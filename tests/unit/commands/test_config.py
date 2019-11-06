from pathlib import Path
from unittest import mock

import click
import yaml
from click.testing import CliRunner

from esque.cli.commands import config_edit, config_migrate
from esque.config import Config, migration
from esque.config.migration import CURRENT_VERSION, get_config_version, migrate
from tests.conftest import config_loader, config_path_mocker


def test_migrate_config(
    mocker: mock, interactive_cli_runner: CliRunner, load_config: config_loader, mock_config_path: config_path_mocker
):
    conf_path, old_conf_text = load_config(0)
    assert get_config_version(conf_path) == CURRENT_VERSION - 1
    mock_config_path(conf_path)

    new_conf_path = conf_path
    backup = None

    def migration_wrapper(config_path: Path):
        nonlocal new_conf_path, backup
        new_conf_path, backup = migrate(config_path)
        return new_conf_path, backup

    mocker.patch.object(migration, "migrate", wraps=migration_wrapper)

    result = interactive_cli_runner.invoke(config_migrate)

    assert result.exit_code == 0
    assert get_config_version(new_conf_path) == CURRENT_VERSION
    assert backup.read_text() == old_conf_text


def test_edit_config(
    mocker: mock, interactive_cli_runner: CliRunner, load_config: config_loader, mock_config_path: config_path_mocker
):
    conf_path, old_conf_text = load_config()
    mock_config_path(conf_path)
    data = yaml.safe_load(old_conf_text)
    data["contexts"]["dupe"] = data["contexts"]["context_1"]
    mocker.patch.object(click, "edit", return_value=yaml.dump(data))

    result = interactive_cli_runner.invoke(config_edit)
    assert result.exit_code == 0
    config = Config()
    assert "dupe" in config.available_contexts