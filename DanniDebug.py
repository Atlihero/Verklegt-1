from ui_layer.OrganizerUI import OrganizerUI

def main():
    print("=== Manual Test: Create Tournament ===\n")

    ui = OrganizerUI()
    result = ui.createTournament()

    print("\n=== Result from LL_API ===")
    print(result)

if __name__ == "__main__":
    main()