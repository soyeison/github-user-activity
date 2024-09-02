import argparse
from integrations.github import GuthubIntegration

def main():
    parser = argparse.ArgumentParser(description="Consult your github profile")

    parser.add_argument('operation', choices=['github-activity'], help="Available operation")
    parser.add_argument('data', type=str, nargs='*')

    args = parser.parse_args()

    try:
        if args.operation == 'github-activity':
            # Validar primero que si se envie la informacion que es via cli
            githubInstance = GuthubIntegration('baseurl')
            print(githubInstance.getUserInformation())
    except:
        print("Melo")

if __name__ == '__main__':
    main()