import traceback
from workflow.agents.agent import Agent

from workflow.agents.evaluator.tool_kit.qd_evaluator import QDEvaluator


class Evaluator(Agent):
    """
    Agent responsible for selecting appropriate schemas based on the context.
    """
    
    def __init__(self, config: dict):
        """Initialize the tools needed for schema selection"""
        super().__init__(
            name="evaluator",
            task="",
            config=config,
        )

        self.tools = {}

        if "qd_evaluator" in config["tools"]:
            print("Inside QD Evaluator!!!")
            self.tools["qd_evaluator"] = QDEvaluator(**config["tools"]["qd_evaluator"])

        print("Inside Evaluator!!!")