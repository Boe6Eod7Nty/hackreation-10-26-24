from model import Model 
from view import View
from presenter import Presenter



try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        '''Nothin'''

 
def main() -> None:
    '''Build the application.'''
    
    model = Model()
    view = View()
    presenter = Presenter(model,view)
    presenter.RunUI()


if __name__ == "__main__":
    main()