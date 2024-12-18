from data.recipes import REGULAR_COCKTAILS
from simulation.party_simulator import PartySimulator

def main():
    simulator = PartySimulator(REGULAR_COCKTAILS)
    simulator.run_multiple(10000)

if __name__ == "__main__":
    main() 