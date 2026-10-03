"""
Personal Mini-Toolkit
---------------------
A menu-driven program with four tools:
  1. Number Guessing Game
  2. To-Do List
  3. Simple Calculator
  4. Countdown Timer

Run it with:  python toolkit.py
"""

import random
import time


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def ask_for_number(prompt):
    """Ask until the user types a valid number. Returns a float, or None if
    the user types 'q' to cancel."""
    while True:
        text = input(prompt).strip()
        if text.lower() == "q":
            return None
        try:
            return float(text)
        except ValueError:
            print(f'  "{text}" is not a number. Try again (or type q to cancel).')


def format_number(value):
    """Show 5.0 as 5, but keep 2.5 as 2.5, so results look friendly."""
    if value == int(value):
        return str(int(value))
    return f"{value:.4f}".rstrip("0").rstrip(".")


# ---------------------------------------------------------------------------
# Tool 1: Number Guessing Game
# Picks a secret number from 1-100 and gives the player 7 tries, with
# "too high" / "too low" hints. Uses a loop, conditionals and try/except.
# ---------------------------------------------------------------------------

def guessing_game():
    max_attempts = 7
    print("\n--- Number Guessing Game ---")

    play_again = "y"
    while play_again == "y":
        secret = random.randint(1, 100)
        attempts_used = 0
        won = False
        print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} tries!")

        while attempts_used < max_attempts and not won:
            guess_text = input(f"Guess #{attempts_used + 1}: ").strip()

            # Make sure the guess is a whole number inside the range
            try:
                guess = int(guess_text)
            except ValueError:
                print(f'  "{guess_text}" is not a whole number. That did not cost you a try.')
                continue
            if guess < 1 or guess > 100:
                print("  Please guess between 1 and 100. That did not cost you a try.")
                continue

            attempts_used += 1
            remaining = max_attempts - attempts_used

            if guess == secret:
                won = True
                print(f"  Correct! You got it in {attempts_used} "
                      f"{'try' if attempts_used == 1 else 'tries'}!")
            elif guess < secret:
                print(f"  Too low! {remaining} {'try' if remaining == 1 else 'tries'} left.")
            else:
                print(f"  Too high! {remaining} {'try' if remaining == 1 else 'tries'} left.")

        if not won:
            print(f"  Out of tries. The secret number was {secret}. Better luck next time!")

        play_again = input("Play again? (y/n): ").strip().lower()

    print("Thanks for playing! Returning to the main menu...")


# ---------------------------------------------------------------------------
# Tool 2: To-Do List
# Keeps a list of tasks that grows and shrinks while the program runs.
# Uses a list (append / pop / enumerate), a loop and conditionals.
# The list is created in main() so tasks are kept when you come back later.
# ---------------------------------------------------------------------------

def show_tasks(tasks):
    """Print the tasks as a numbered list with a done/not-done marker."""
    if len(tasks) == 0:
        print("  Your to-do list is empty. Nice and clean!")
        return
    print("  Your tasks:")
    for number, task in enumerate(tasks, start=1):
        marker = "[x]" if task["done"] else "[ ]"
        print(f"    {number}. {marker} {task['name']}")


def pick_task_number(tasks, action):
    """Ask which task to act on. Returns a list index, or None if invalid."""
    show_tasks(tasks)
    text = input(f"  Which task number do you want to {action}? ").strip()
    if not text.isdigit() or not 1 <= int(text) <= len(tasks):
        print(f'  "{text}" is not a valid task number.')
        return None
    return int(text) - 1


def todo_list(tasks):
    print("\n--- To-Do List ---")

    while True:
        print("\n  1. Add a task")
        print("  2. View tasks")
        print("  3. Mark a task as done")
        print("  4. Remove a task")
        print("  5. Back to main menu")
        choice = input("  Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("  What is the task? ").strip()
            if name == "":
                print("  A task can't be empty. Nothing was added.")
            else:
                tasks.append({"name": name, "done": False})
                print(f'  Added "{name}". You now have {len(tasks)} '
                      f"{'task' if len(tasks) == 1 else 'tasks'}.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            if len(tasks) == 0:
                print("  There is nothing to mark yet. Add a task first!")
            else:
                index = pick_task_number(tasks, "mark as done")
                if index is not None:
                    tasks[index]["done"] = True
                    print(f'  Great job! "{tasks[index]["name"]}" is done.')
        elif choice == "4":
            if len(tasks) == 0:
                print("  There is nothing to remove.")
            else:
                index = pick_task_number(tasks, "remove")
                if index is not None:
                    removed = tasks.pop(index)
                    print(f'  Removed "{removed["name"]}". {len(tasks)} left.')
        elif choice == "5":
            print("  Returning to the main menu...")
            break
        else:
            print(f'  "{choice}" is not an option. Please type a number from 1 to 5.')


# ---------------------------------------------------------------------------
# Tool 3: Simple Calculator
# Takes two numbers and an operation, then prints the answer. Uses
# conditionals to pick the operation and to avoid dividing by zero.
# ---------------------------------------------------------------------------

def calculator():
    print("\n--- Simple Calculator ---")
    print("Type q at any number prompt to go back.")

    while True:
        first = ask_for_number("\nFirst number: ")
        if first is None:
            break
        second = ask_for_number("Second number: ")
        if second is None:
            break

        operation = input("Operation (+, -, *, /): ").strip()

        if operation == "+":
            result = first + second
        elif operation == "-":
            result = first - second
        elif operation == "*":
            result = first * second
        elif operation == "/":
            if second == 0:
                result = None
                print("  Oops! You can't divide by zero.")
            else:
                result = first / second
        else:
            result = None
            print(f'  "{operation}" is not a supported operation. Use +, -, * or /.')

        if result is not None:
            print(f"  {format_number(first)} {operation} {format_number(second)} "
                  f"= {format_number(result)}")

        again = input("Calculate again? (y/n): ").strip().lower()
        if again != "y":
            break

    print("Returning to the main menu...")


# ---------------------------------------------------------------------------
# Tool 4: Countdown Timer
# Counts down from a number of seconds (1-30) chosen by the user. Uses a
# for loop with range() running backwards, plus input validation.
# ---------------------------------------------------------------------------

def countdown_timer():
    print("\n--- Countdown Timer ---")
    text = input("How many seconds should I count down from (1-30)? ").strip()

    if not text.isdigit():
        print(f'  "{text}" is not a whole number, so no countdown this time.')
    elif int(text) < 1 or int(text) > 30:
        print("  Please pick a number between 1 and 30.")
    else:
        seconds = int(text)
        print(f"  Starting a {seconds}-second countdown...")
        for remaining in range(seconds, 0, -1):
            print(f"  {remaining}...")
            time.sleep(1)
        print("  Time's up! Ding ding ding!")

    print("Returning to the main menu...")


# ---------------------------------------------------------------------------
# Main menu
# Shows the menu in a loop and routes each choice with if / elif / else.
# The loop only stops when the user chooses Quit.
# ---------------------------------------------------------------------------

def show_menu():
    print("\n==============================")
    print("   PERSONAL MINI-TOOLKIT")
    print("==============================")
    print("1. Number Guessing Game")
    print("2. To-Do List")
    print("3. Simple Calculator")
    print("4. Countdown Timer")
    print("5. Quit")
    print("------------------------------")


def main():
    tasks = []  # shared to-do list so tasks survive going back to the menu

    print("Welcome to your Personal Mini-Toolkit! Pick a tool to get started.")

    running = True
    while running:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            guessing_game()
        elif choice == "2":
            todo_list(tasks)
        elif choice == "3":
            calculator()
        elif choice == "4":
            countdown_timer()
        elif choice == "5":
            running = False
        else:
            print(f'\nOops! "{choice}" is not on the menu. Please type a number from 1 to 5.')

    print("\nThanks for using the toolkit. Goodbye and see you next time!")


# Only run the program when this file is executed directly
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nToolkit closed. Goodbye!")