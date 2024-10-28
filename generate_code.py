import subprocess


def run_openhands(prompt):
    cmd = ['./run_openhands.sh', prompt]

    try:
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        print('Command output:')
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print('An error occurred:')
        print(f'Exit code: {e.returncode}')
        print(f'Error output: {e.stderr}')
    except FileNotFoundError:
        print('The script run_openhands.sh was not found.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')


if __name__ == '__main__':
    prompt_text = 'write a bash script that prints hi'
    run_openhands(prompt_text)
