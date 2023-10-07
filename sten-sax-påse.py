import random

def get_valid_player_choice():
    while True:
        spelarens_drag = input("Välj mellan (sten,sax,påse): ").lower()
        if spelarens_drag in ["sten","sax","påse"]:
            return spelarens_drag
        else:
            print("Fel inmatning. Välj enbart sten, sax eller påse.")

def main():
    drag = ["sten", "sax", "påse"]

    while True:
        datorn = random.choice(drag)
        spelarens_drag = get_valid_player_choice()

        print(f"Spelare: {spelarens_drag}")
        print(f"Datorn: {datorn}")

        winning_conditions = {
            ("sten", "sax"): "Du vann!",
            ("sax", "påse"): "Du vann!",
            ("påse", "sten"): "Du vann!",
        }

        if spelarens_drag == datorn:
            print("Spelet är oavgjort")
        elif (spelarens_drag, datorn) in winning_conditions:
            print(winning_conditions[(spelarens_drag, datorn)])
            break  # Player wins, exit the loop
        else:
            print("Datorn vann!")

        play_again = input("Vill du spela igen? (ja/nej): ").strip().lower()
        if play_again != "ja":
            print("Tack för att du spelade!")
            break

if __name__ == "__main__":
    main()