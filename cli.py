import argparse
import config
from integrations.github import GuthubIntegration

def main():
    parser = argparse.ArgumentParser(description="Consult your github profile")

    parser.add_argument('operation', choices=['github-activity'], help="Available operation")
    parser.add_argument('data', type=str, nargs='*')

    args = parser.parse_args()

    try:
        if args.operation == 'github-activity':
            # Validar primero que si se envie la informacion que es via cli
            githubInstance = GuthubIntegration(config.GITHUB_BASE_URL)
            print(githubInstance.getUserInformation("soyeison"))
    except:
        print("Melo")

if __name__ == '__main__':
    main()