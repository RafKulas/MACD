from classes.human import Human
from classes.data import Data
from classes.controller import Controller
from sys import argv
from matplotlib import pyplot

if __name__ == '__main__':
    if argv[1] != "--help" and argv[1] != "-h":
        name = "spolki/" + argv[1]
        data = Data(name)
        human = Human(data)
        stock = None

        if len(argv) == 3:
            stock = Controller(data, human, int(argv[2]))  # Jesli argv[3] = 1 to Controller uzyje uzyje lekko
            # ulepszonej wersji wskaźnika a jesli argv[3] > 1 to ulepszonej wersji
        else:
            stock = Controller(data, human)

        stock.stock()

        date = data.getDate()
        # pyplot.figure("Project")
        # pyplot.subplot(2, 1, 1)
        # pyplot.plot(date, data.getClose(), label="Price", color="green")
        # pyplot.ylabel("Price in USD")
        # pyplot.xlabel("Date in yyyy-mm-dd format")
        # pyplot.title("Price")
        # pyplot.legend()
        # pyplot.grid(True)
        # pyplot.subplot(2, 1, 2)
        # pyplot.plot(date, data.getMACD(), label="MACD", color="red")
        # pyplot.plot(date, data.getSignal(), label="Signal", color="blue")
        # pyplot.ylabel("Indicator value")
        # pyplot.xlabel("Date in yyyy-mm-dd format")
        # pyplot.title("MACD and Signal")
        # pyplot.legend()
        # pyplot.tight_layout(h_pad=1)
        # pyplot.grid(True)
        # pyplot.show()

        pyplot.figure("Project")          # rysowanie wykresu różnicy
        pyplot.plot(date, data.getDiff(), label="Difference", color="green")
        pyplot.title("Difference")
        pyplot.legend()
        pyplot.axhline(linewidth=2, color='red')
        pyplot.xlabel("Date in yyyy-mm-dd format")
        pyplot.ylabel("Different value")
        pyplot.grid(True)
        pyplot.show()


    else:
        print("\n" + "#"*48)
        print("#___________MACD usage with CSV file___________#")
        print("#_____First argument is for source CSV file____#")
        print("#_____Second argument is delay in days from____#\n"
              "#___buying or selling when two lines crosses___#")
        print("#___Third argument is set to over zero when____#\n"
              "#____you want to use better version of MACD____#")
        print("#"*48 + "\n")
