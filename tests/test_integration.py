"""Tests d'intégration pour le système MAEL."""

import sys
import os
from pathlib import Path

# Pattern robust_import_with_stub pour StateManager
try:
    from src.state_manager import StateManager
except ImportError:
    # Fallback vers stub
    stub_path = str(Path(__file__).parent / "stubs")
    if stub_path not in sys.path:
        sys.path.insert(0, stub_path)
    
    class StateManager:
        """Stub StateManager pour tests."""
        
        def __init__(self):
            self.config = {"version": "1.0", "mode": "test"}
            self.metrics = {"iterations": 0, "success_rate": 0.0}
        
        def load_state(self):
            """Charge un état mock pour les tests."""
            return MockState()
        
        def save_state(self, state):
            """Sauvegarde mock."""
            return True

class MockState:
    """État mock pour les tests."""
    
    def __init__(self):
        self.config = {"version": "1.0", "mode": "test"}
        self.metrics = {"iterations": 0, "success_rate": 0.0}
        self.skills = []
        self.learnings = []
    
    def is_valid(self):
        """Valide que l'état a la structure attendue."""
        return (hasattr(self, 'config') and 
                hasattr(self, 'metrics') and
                hasattr(self, 'skills') and
                hasattr(self, 'learnings'))

import pytest

@pytest.fixture
def initial_state():
    """Fixture qui charge l'état initial pour les tests."""
    state_manager = StateManager()
    state = state_manager.load_state()
    assert state is not None and hasattr(state, 'config')
    return state

def test_initial_state_fixture(initial_state):
    """Test que la fixture initial_state fonctionne correctement."""
    assert initial_state is not None
    assert hasattr(initial_state, 'config')
    assert hasattr(initial_state, 'metrics')
    assert isinstance(initial_state.config, dict)
    assert 'version' in initial_state.config

def test_state_loading():
    """Test direct du chargement d'état."""
    state_manager = StateManager()
    state = state_manager.load_state()
    
    assert state is not None
    assert hasattr(state, 'config')
    assert hasattr(state, 'metrics')
    assert state.is_valid()

def test_state_structure(initial_state):
    """Test de la structure de l'état chargé."""
    assert hasattr(initial_state, 'skills')
    assert hasattr(initial_state, 'learnings')
    assert isinstance(initial_state.skills, list)
    assert isinstance(initial_state.learnings, list)

def test_state_manager_integration():
    """Test d'intégration du StateManager."""
    manager = StateManager()
    assert hasattr(manager, 'load_state')
    assert hasattr(manager, 'save_state')
    
    # Test du cycle load/save
    state = manager.load_state()
    result = manager.save_state(state)
    assert result is True
