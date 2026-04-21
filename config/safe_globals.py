import typing
from collections import OrderedDict, defaultdict

import torch
from omegaconf import DictConfig, ListConfig
from omegaconf.base import ContainerMetadata, Metadata
from omegaconf.nodes import AnyNode, BooleanNode, FloatNode, IntegerNode, StringNode
from pyannote.audio.core.model import Introspection
from pyannote.audio.core.task import Problem, Resolution, Specifications
from torch.torch_version import TorchVersion


def setup_torch_safe_globals():
    """Autorize OmegaConf types required by Pyannote for torch>=2.6."""
    torch.serialization.add_safe_globals(
        [
            DictConfig,
            ListConfig,
            ContainerMetadata,
            Metadata,
            AnyNode,
            BooleanNode,
            FloatNode,
            IntegerNode,
            StringNode,
            typing.Any,
            list,
            dict,
            tuple,
            set,
            frozenset,
            int,
            float,
            bool,
            str,
            bytes,
            OrderedDict,
            defaultdict,
            TorchVersion,
            Introspection,
            Specifications,
            Problem,
            Resolution,
        ]
    )
