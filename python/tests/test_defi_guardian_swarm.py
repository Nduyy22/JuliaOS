"""
Test Suite for DeFi Guardian Swarm System

This test suite validates the core functionality of the DeFi Guardian Swarm
built on the JuliaOS framework.

Usage:
    pytest python/tests/test_defi_guardian_swarm.py -v
"""

import pytest
import asyncio
import os
from unittest.mock import Mock, patch
import sys

# Add the python/src directory to Python path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
python_src_path = os.path.join(project_root, 'python', 'src')
python_scripts_path = os.path.join(project_root, 'python', 'scripts')

sys.path.insert(0, python_src_path)
sys.path.insert(0, python_scripts_path)

# Ensure the script directory is in sys.path for import resolution
if python_scripts_path not in sys.path:
    sys.path.insert(0, python_scripts_path)

# Import the main components using importlib to avoid Pylance errors
import importlib.util

# Load the run_defi_guardian_swarm module dynamically
script_path = os.path.join(python_scripts_path, "run_defi_guardian_swarm.py")
spec = importlib.util.spec_from_file_location("run_defi_guardian_swarm", script_path)
run_defi_guardian_swarm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(run_defi_guardian_swarm)

# Extract the functions we need
create_risk_management_agents = run_defi_guardian_swarm.create_risk_management_agents
create_mev_protection_agents = run_defi_guardian_swarm.create_mev_protection_agents
create_governance_agents = run_defi_guardian_swarm.create_governance_agents
create_coordinator_agent = run_defi_guardian_swarm.create_coordinator_agent

class TestDeFiGuardianSwarm:
    """Test class for DeFi Guardian Swarm functionality"""
    
    def test_risk_management_agents_creation(self):
        """Test that risk management agents are properly configured"""
        agents = create_risk_management_agents()
        
        # Should create 3 risk management agents
        assert len(agents) == 3
        
        # Check agent types
        agent_types = [agent[0] for agent in agents]
        expected_types = ["portfolio-risk-analyzer", "liquidity-monitor", "volatility-tracker"]
        
        for expected_type in expected_types:
            assert expected_type in agent_types
        
        # Validate agent configurations
        for agent_id, name, description, blueprint in agents:
            assert agent_id is not None
            assert name is not None
            assert description is not None
            assert blueprint is not None
            
            # Check blueprint structure
            assert hasattr(blueprint, 'tools')
            assert hasattr(blueprint, 'strategy')
            assert hasattr(blueprint, 'trigger')
            
            # Verify LLM chat tool is included
            tool_names = [tool.name for tool in blueprint.tools]
            assert "llm_chat" in tool_names
    
    def test_mev_protection_agents_creation(self):
        """Test that MEV protection agents are properly configured"""
        agents = create_mev_protection_agents()
        
        # Should create 3 MEV protection agents
        assert len(agents) == 3
        
        # Check agent types
        agent_types = [agent[0] for agent in agents]
        expected_types = ["mempool-scanner", "sandwich-detector", "tx-optimizer"]
        
        for expected_type in expected_types:
            assert expected_type in agent_types
        
        # Validate MEV-specific configurations
        for agent_id, name, description, blueprint in agents:
            assert "mev" in description.lower() or "sandwich" in description.lower() or "mempool" in description.lower()
            
            # Check strategy configuration
            strategy_config = blueprint.strategy.config
            assert "specialization" in strategy_config
            
            mev_specializations = [
                "mempool_threat_detection",
                "sandwich_attack_prevention", 
                "mev_resistant_execution"
            ]
            assert strategy_config["specialization"] in mev_specializations
    
    def test_governance_agents_creation(self):
        """Test that governance agents are properly configured"""
        agents = create_governance_agents()
        
        # Should create 3 governance agents
        assert len(agents) == 3
        
        # Check agent types
        agent_types = [agent[0] for agent in agents]
        expected_types = ["proposal-analyzer", "sentiment-monitor", "voting-optimizer"]
        
        for expected_type in expected_types:
            assert expected_type in agent_types
        
        # Validate governance-specific configurations
        for agent_id, name, description, blueprint in agents:
            assert any(keyword in description.lower() for keyword in 
                      ["governance", "proposal", "voting", "sentiment", "dao"])
            
            # Check strategy configuration
            strategy_config = blueprint.strategy.config
            assert "specialization" in strategy_config
            
            governance_specializations = [
                "dao_proposal_evaluation",
                "community_sentiment_analysis",
                "optimal_voting_strategy"
            ]
            assert strategy_config["specialization"] in governance_specializations
    
    def test_coordinator_agent_creation(self):
        """Test that coordinator agent is properly configured"""
        coordinator = create_coordinator_agent()
        
        assert coordinator is not None
        assert hasattr(coordinator, 'tools')
        assert hasattr(coordinator, 'strategy')
        assert hasattr(coordinator, 'trigger')
        
        # Check coordinator-specific configuration
        strategy_config = coordinator.strategy.config
        assert strategy_config["specialization"] == "multi_swarm_coordination"
        assert "coordination_priorities" in strategy_config
        assert "decision_types" in strategy_config
        assert "consensus_threshold" in strategy_config
        
        # Validate priority levels
        priorities = strategy_config["coordination_priorities"]
        assert priorities["critical"] == 1
        assert priorities["high"] == 2
        assert priorities["medium"] == 3
        assert priorities["low"] == 4
        
        # Validate decision types
        decision_types = strategy_config["decision_types"]
        expected_decisions = [
            "emergency_stop", "rebalance_portfolio", "block_transaction",
            "alert_user", "vote_proposal", "update_strategy"
        ]
        for decision in expected_decisions:
            assert decision in decision_types
    
    def test_agent_blueprint_consistency(self):
        """Test that all agent blueprints follow consistent patterns"""
        all_agent_creators = [
            create_risk_management_agents,
            create_mev_protection_agents,
            create_governance_agents
        ]
        
        for creator_func in all_agent_creators:
            agents = creator_func()
            
            for agent_id, name, description, blueprint in agents:
                # All agents should have LLM chat capability
                tool_names = [tool.name for tool in blueprint.tools]
                assert "llm_chat" in tool_names
                
                # All agents should have webhook trigger
                assert blueprint.trigger.type == "webhook"
                
                # All strategies should have specialization
                assert "specialization" in blueprint.strategy.config
                
                # Agent IDs should be kebab-case
                assert "-" in agent_id
                assert agent_id.islower()
    
    @pytest.mark.asyncio
    async def test_system_integration_mock(self):
        """Test system integration with mocked JuliaOS connection"""
        
        # Mock the JuliaOS connection and agent creation
        with patch('juliaos.JuliaOSConnection') as mock_connection:
            with patch('juliaos.Agent') as mock_agent:
                
                # Setup mocks
                mock_conn = Mock()
                mock_connection.return_value.__enter__.return_value = mock_conn
                mock_conn.list_agents.return_value = []
                
                mock_agent_instance = Mock()
                mock_agent_instance.id = "test-agent"
                mock_agent.create.return_value = mock_agent_instance
                
                # Test that we can create all agent types without errors
                risk_agents = create_risk_management_agents()
                mev_agents = create_mev_protection_agents()
                governance_agents = create_governance_agents()
                coordinator = create_coordinator_agent()
                
                # Verify we have the expected number of agents
                total_swarm_agents = len(risk_agents) + len(mev_agents) + len(governance_agents)
                assert total_swarm_agents == 9  # 3 per swarm
                assert coordinator is not None
    
    def test_configuration_validation(self):
        """Test that agent configurations are valid for the expected use cases"""
        
        # Test risk management specializations
        risk_agents = create_risk_management_agents()
        risk_specializations = []
        for _, _, _, blueprint in risk_agents:
            risk_specializations.append(blueprint.strategy.config["specialization"])
        
        expected_risk_specs = [
            "portfolio_risk_assessment",
            "liquidity_risk_assessment", 
            "market_volatility_tracking"
        ]
        for spec in expected_risk_specs:
            assert spec in risk_specializations
        
        # Test MEV protection configurations
        mev_agents = create_mev_protection_agents()
        mev_configs = []
        for _, _, _, blueprint in mev_agents:
            config = blueprint.strategy.config
            mev_configs.append(config)
            
            # Each MEV agent should have detection/protection mechanisms
            if "detection" in config["specialization"]:
                assert any(key in config for key in ["detection_algorithms", "detection_methods"])
        
        # Test governance configurations
        governance_agents = create_governance_agents()
        governance_configs = []
        for _, _, _, blueprint in governance_agents:
            config = blueprint.strategy.config
            governance_configs.append(config)
            
            # Governance agents should have relevant frameworks/sources
            if "analysis" in config["specialization"]:
                assert any(key in config for key in ["analysis_frameworks", "monitoring_sources"])
    
    def test_agent_naming_conventions(self):
        """Test that agent names follow proper conventions"""
        all_creators = [
            create_risk_management_agents,
            create_mev_protection_agents, 
            create_governance_agents
        ]
        
        for creator in all_creators:
            agents = creator()
            for agent_id, name, description, blueprint in agents:
                # Agent IDs should be lowercase with hyphens
                assert agent_id.islower()
                assert "-" in agent_id
                
                # Names should be title case
                assert name[0].isupper()
                
                # Descriptions should be descriptive
                assert len(description) > 10
                assert description[0].isupper()

class TestDeFiGuardianIntegration:
    """Integration tests for the complete DeFi Guardian system"""
    
    def test_agent_count_totals(self):
        """Test that we have the correct total number of agents"""
        risk_agents = create_risk_management_agents()
        mev_agents = create_mev_protection_agents()
        governance_agents = create_governance_agents()
        
        # Should have 9 total swarm agents + 1 coordinator
        assert len(risk_agents) == 3
        assert len(mev_agents) == 3
        assert len(governance_agents) == 3
        
        total_swarm_agents = len(risk_agents) + len(mev_agents) + len(governance_agents)
        assert total_swarm_agents == 9
    
    def test_unique_agent_ids(self):
        """Test that all agent IDs are unique"""
        all_agents = []
        
        # Collect all agent IDs
        for creator in [create_risk_management_agents, create_mev_protection_agents, create_governance_agents]:
            agents = creator()
            all_agents.extend([agent[0] for agent in agents])
        
        # Add coordinator
        all_agents.append("defi-coordinator-agent")  # From the main script
        
        # Check uniqueness
        assert len(all_agents) == len(set(all_agents))
    
    def test_swarm_specialization_coverage(self):
        """Test that we cover all major DeFi protection areas"""
        
        # Risk management coverage
        risk_agents = create_risk_management_agents()
        risk_areas = [blueprint.strategy.config["specialization"] for _, _, _, blueprint in risk_agents]
        
        expected_risk_areas = ["portfolio", "liquidity", "volatility"]
        for area in expected_risk_areas:
            assert any(area in spec for spec in risk_areas)
        
        # MEV protection coverage
        mev_agents = create_mev_protection_agents()
        mev_areas = [blueprint.strategy.config["specialization"] for _, _, _, blueprint in mev_agents]
        
        expected_mev_areas = ["mempool", "sandwich", "optimization"]
        for area in expected_mev_areas:
            assert any(area in spec for spec in mev_areas)
        
        # Governance coverage
        governance_agents = create_governance_agents()
        governance_areas = [blueprint.strategy.config["specialization"] for _, _, _, blueprint in governance_agents]
        
        expected_governance_areas = ["proposal", "sentiment", "voting"]
        for area in expected_governance_areas:
            assert any(area in spec for spec in governance_areas)

if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
