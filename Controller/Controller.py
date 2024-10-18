from Controller.ModelController import ModelController
from Controller.ViewController import ViewController

# This class contains all the different settings of the program and
# is used as a link between the models and the views
class Controller():
    def __init__(self, view_controller:ViewController, model_controller:ModelController) -> None:
        self.view_controller = view_controller
        self.model_controller = model_controller
        
        # Settings initialization
        self.RECORD_LENGHT:int = 0
        self.PRE_TRIGGER:int = 0
    
    # --- Useful functions for changing/getting experiment parameters --- #
    """ def get_rcd_len(self) -> int:
        return self.RECORD_LENGHT
    def set_rcd_len(self, x: int) -> None:
        self.RECORD_LENGHT = x
    def get_pre_trigger(self) -> int:
        return self.PRE_TRIGGER
    def set_pre_trigger(self, x:int) -> None:
        self.PRE_TRIGGER """
    # ------------------------------------------------------------------- #
    
    # Getting information from the models
    def get_data_analyser(self):
        return self.model_controller.get_data_analyser()
        
    # From models to views
    def send_feedback(self, message:str):
        self.view_controller