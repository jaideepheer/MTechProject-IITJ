from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Callable, Dict, List, Optional
from hydra.core.config_store import ConfigStore


class RunMode(Enum):
    default = auto
    experiment = auto
    debug = auto


@dataclass
class IgniteLoggerHandler:
    event: Any
    log_handler: Any


@dataclass
class IgniteLogger:
    logger: Any
    handlers: Dict[str, IgniteLoggerHandler]


@dataclass
class RunConfig:
    # path to original working directory
    # https://hydra.cc/docs/next/tutorials/basic/running_your_app/working_directory
    work_dir: str
    # path to dataset directory
    data_dir: str
    # the mode of the run to decide directories and other settings
    run_mode: RunMode
    # disable python warnings if they annoy you
    ignore_warnings: bool
    # seed for random number generators in pytorch, tensorflow, numpy and python.random
    seed: Optional[int]
    # name of the run is accessed by loggers
    # should be used along with experiment mode
    name: Optional[str]
    # print config
    print_config: bool
    # dict of loggers to use
    loggers: Optional[Dict[str, IgniteLogger]]


@dataclass
class IgniteHandler:
    handler: Callable
    event: Optional[Any]
    kwargs: Optional[Any]


@dataclass
class TrainConfig(RunConfig):
    # the device to train on
    device: Optional[str]
    # datamodule
    datamodule: Any
    # trainer
    trainer: Any
    # event handlers
    handlers: Optional[Dict[str, Any]]
    # model
    model: Any
    max_epochs: int


cs = ConfigStore.instance()
cs.store("default_run_config", node=RunConfig)
cs.store("default_train_config", node=TrainConfig)
