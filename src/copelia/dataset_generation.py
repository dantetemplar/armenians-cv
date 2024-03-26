from pathlib import Path
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

from src.copelia.config import Config

settings = Config.from_yaml(Path(__file__).parent / "config.yaml")


class CustomRemoteAPIClient(RemoteAPIClient):
    def _process_response(self, resp):
        ret = resp["ret"]
        if len(ret) == 1:
            # serialize to numpy when possible
            if isinstance(ret[0], list):
                return np.array(ret[0])
            return ret[0]
        if len(ret) > 1:
            return tuple(ret)


client = CustomRemoteAPIClient()
sim = client.getObject("sim")

# Load the scene
scene_path = Path(__file__).parent / "generateDataset.ttt"
scene_path = scene_path.resolve()
sim.loadScene(str(scene_path.absolute()))

# Load scripts
helicopterHandle = sim.getObject("/Helicopter")
helicopterScriptsHandle: int = sim.getScript(sim.scripttype_childscript, helicopterHandle)
helicopterScripts = client.getScriptFunctions(helicopterScriptsHandle)

# Start the simulation
sim.startSimulation()
try:
    # Get the handle of the helicopter target
    helicopter_target = sim.getObject("./target")

    markers = iter(settings.markers)
    marker = next(markers, None)

    # move the helicopter target (do not change z position)
    while marker and ((t := sim.getSimulationTime()) < settings.timeout):
        # check if the helicopter has reached the target
        helicopter_position = sim.getObjectPosition(helicopterHandle)
        helicopter_target_position = sim.getObjectPosition(helicopter_target)
        dist = np.linalg.norm(helicopter_position - helicopter_target_position)
        if dist < settings.marker_radius:
            print(f"Helicopter reached the target at {t:.2f} [s]")
            marker = next(markers, None)
            if marker is None:
                sim.pauseSimulation()
                break
            helicopterScripts.moveTarget(marker)
        sim.step()
except Exception as e:
    # Stop the simulation
    sim.stopSimulation()
    raise e
