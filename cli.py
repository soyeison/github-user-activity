import argparse
import config
from utils.format_user_activity import formatUserActivity
from integrations.github.github import GuthubIntegration
from errors.number_of_argument_exception import NumberOfArgumentException
from errors.invalid_username_exception import InvalidUsernameException

def main():
    parser = argparse.ArgumentParser(description="Consult your github profile")

    parser.add_argument('operation', choices=['github-activity'], help="Available operation")
    parser.add_argument('data', type=str, nargs='*')

    args = parser.parse_args()

    try:
        if args.operation == 'github-activity':
            # Validar primero que si se envie la informacion que es via cli
            if len(args.data) == 0 or len(args.data) >= 2:
                raise NumberOfArgumentException()

            githubInstance = GuthubIntegration(config.GITHUB_BASE_URL)
            userActivity = githubInstance.getUserInformation(args.data[0])
            userActivityFormated = formatUserActivity(userActivity)
            
            # Mostrar por consola
            for userActivity in userActivityFormated:
                print(userActivity)

    except InvalidUsernameException as e:
        print(f"Error: {e}")
    except NumberOfArgumentException as e:
        print(f"Error: {e}")
    except:
        print("Melo")

if __name__ == '__main__':
    main()