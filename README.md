> Система детекции и лоцирование буквенных символов на изображении с квадрокоптера

## Содержание

GitHub поддерживает генерацию
содержания [по умолчанию](https://github.blog/changelog/2021-04-13-table-of-contents-support-in-markdown-files/) 🤔

### Технологии

- [Python 3.10](https://www.python.org/downloads/release/python-31011/) & [Mamba](https://mamba.readthedocs.io/en/latest/index.html)
- Core ML: [PyTorch](https://pytorch.org/)
- Plotting: [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)
- Code quality: [Ruff](https://docs.astral.sh/ruff/) & [Pre-commit](https://pre-commit.com/)

## Разработка

### Начало работы

1. Установите [Mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html)  и [Conda-Lock](https://github.com/conda/conda-lock)
2. Установите зависимости проекта из lock файла
   ```bash
    mamba create -n armenians_cv --file conda-linux-64.lock
   ```
3. Активируйте окружение
   ```bash
   mamba activate armenians_cv
   ```
4. Настройте [pre-commit](https://pre-commit.com/) хуки:
   ```bash
   pre-commit install --install-hooks -t pre-commit -t commit-msg
   ```

**Интеграции в PyCharm**

1. Ruff ([plugin](https://plugins.jetbrains.com/plugin/20574-ruff))
2. Conventional commits ([plugin](https://plugins.jetbrains.com/plugin/13389-conventional-commit))


### FAQ

**Как обновить lock файл?**

```bash
conda-lock --mamba
```

**Как сохранить зависимости для определенной ОС?**

```bash
conda-lock render --mamba --platform linux-64
```

**Как обновить зависимости из lock файла?**

```bash
mamba env update -n armenians_cv --file conda-linux-64.lock
```
