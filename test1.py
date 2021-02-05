#!/usr/bin/python3

import os

def main():
    
    pr_dir = None
    repo_dir = None

    print("This PR is adding/changing {} files:".format(os.listdir(pr_dir)))

    for filename in os.listdir(pr_dir):
        print(filename)

    print("")

    print("The repo has {} files:".format(os.listdir(repo_dir)))

    for filename in os.listdir(repo_dir):
        print(filename)


if __name__ == "__main__":
    main()