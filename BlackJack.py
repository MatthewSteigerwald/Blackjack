import random
import tkinter as tk
from PIL import Image, ImageTk 
from PIL import ImageEnhance
import time

# Global variables
window = None
player_balance = 2500
player_bet = 0
dealer_hidden_card_index = None
deck = []
player_hand = [[], []]
dealer_hand = [[], []]
player_count = 0
dealer_count = 0
card_labels = []
casino_chip_images = []

# Visual elements
message_label = None
balance_label = None
bet_label = None
deal_button = None
hit_button = None
stand_button = None
double_down_button = None
shuffle_button = None
red_chip_button = None
green_chip_button = None
blue_chip_button = None
yellow_chip_button = None
clear_bet_button = None

def setup_window():
    global window, message_label, balance_label, bet_label, casino_chip_images
    
    # Making an array of poker chip images
    casino_chip_images = [r"C:\Users\matth\Desktop\Python\Chips\pokerchip1.png", 
                        r"C:\Users\matth\Desktop\Python\Chips\pokerchip2.png",
                        r"C:\Users\matth\Desktop\Python\Chips\pokerchip3.png", 
                        r"C:\Users\matth\Desktop\Python\Chips\pokerchip4.png"]

    # Making a window
    window = tk.Tk()
    window.title("Blackjack Game")
    window.geometry("1500x1000")
    window.configure(bg="green")
    
    # Showing all the buttons
    show_buttons()
    show_chip_buttons()
    
    # Adding messages, player balance, and player bet labels
    message_label = tk.Label(window, text="", font=('Times New Roman', 20), bg="green", fg="black")
    message_label.pack(pady=10)
    
    balance_label = tk.Label(window, text="", font=('Times New Roman', 30), bg="green", fg="black")
    balance_label.place(x=20, y=20)
    
    bet_label = tk.Label(window, text="Bet:", font=('Times New Roman', 30), bg="green", fg="black")
    bet_label.place(x=20, y=80)
    
    # Showing the players balance
    update_balance("$" + str(player_balance))
    
    # Opening the window
    window.mainloop()

def shuffle_cards():
    global deck
    # Clearing images on window and displaying shuffling
    clear_card_images()
    update_message("Shuffling deck...")
    # waiting for deck to shuffle
    window.after(1000, complete_shuffle)

def complete_shuffle():
    global deck
    # Resetting deal button
    deal_button.config(state="normal")
    # Making an array for each card rank
    ranks = [2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5, 6,6,6,6,
            7,7,7,7, 8,8,8,8, 9,9,9,9, 10,10,10,10,
            'J','J','J','J', 'Q','Q','Q','Q', 'K','K','K','K', 'A','A','A','A']
    # Making an array for each card suit
    suits = ['C','D','H','S'] * 13
    # Making an array containing each card image
    card_images = [r"C:\Users\matth\Desktop\PNG-cards-1.3\2_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\2_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\2_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\2_of_spades.png",
            r"C:\Users\matth\Desktop\PNG-cards-1.3\3_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\3_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\3_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\3_of_spades.png", 
            r"C:\Users\matth\Desktop\PNG-cards-1.3\4_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\4_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\4_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\4_of_spades.png", 
            r"C:\Users\matth\Desktop\PNG-cards-1.3\5_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\5_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\5_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\5_of_spades.png", 
            r"C:\Users\matth\Desktop\PNG-cards-1.3\6_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\6_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\6_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\6_of_spades.png", 
            r"C:\Users\matth\Desktop\PNG-cards-1.3\7_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\7_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\7_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\7_of_spades.png", 
            r"C:\Users\matth\Desktop\PNG-cards-1.3\8_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\8_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\8_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\8_of_spades.png", 
            r"C:\Users\matth\Desktop\PNG-cards-1.3\9_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\9_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\9_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\9_of_spades.png", 
            r"C:\Users\matth\Desktop\PNG-cards-1.3\10_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\10_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\10_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\10_of_spades.png", 
            r"C:\Users\matth\Desktop\PNG-cards-1.3\jack_of_clubs2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\jack_of_diamonds2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\jack_of_hearts2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\jack_of_spades2.png",
            r"C:\Users\matth\Desktop\PNG-cards-1.3\queen_of_clubs2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\queen_of_diamonds2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\queen_of_hearts2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\queen_of_spades2.png",
            r"C:\Users\matth\Desktop\PNG-cards-1.3\king_of_clubs2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\king_of_diamonds2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\king_of_hearts2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\king_of_spades2.png", 
            r"C:\Users\matth\Desktop\PNG-cards-1.3\ace_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\ace_of_diamonds.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\ace_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\ace_of_spades2.png"
               ]
    
    # Combine ranks and suits with images
    deck = [list(zip(ranks, suits)), card_images]
    # Updating message
    update_message("Deck Shuffled")

def deal_cards():
    global player_hand, dealer_hand, dealer_hidden_card_index, player_count, dealer_count
    
    # Clearing window and messages
    clear_card_images()
    update_message("")
    # Disabling deal button while enabling hit, stand, and double down buttons
    deal_button.config(state="disabled")
    hit_button.config(state="normal")
    stand_button.config(state="normal")
    double_down_button.config(state="normal")
    # Disabling betting buttons
    red_chip_button.config(state="disabled")
    green_chip_button.config(state="disabled")
    blue_chip_button.config(state="disabled")
    yellow_chip_button.config(state="disabled")
    
    # Checking if there are enough cards in the shute
    if len(deck[0]) < 8:
        hit_button.config(state='disabled')
        stand_button.config(state='disabled')
        deal_button.config(state='disabled')
        update_message("Shute is over")
        print("Not enough cards left in the deck.")
        clear_card_images()
        return
    
    # Defining both player and dealer hands
    player_hand = [[],[]]
    dealer_hand = [[],[]]
    
    # Adding cards to both player and dealer hand
    for i in range(2):
        card_index = random.randrange(len(deck[0]))
        card = deck[0][card_index]
        player_hand[0].append(card)
        player_hand[1].append(deck[1][card_index])
        deck[0].remove(card)
        deck[1].remove(deck[1][card_index])
    
    for i in range(2):
        card_index = random.randrange(len(deck[0]))
        card = deck[0][card_index]
        dealer_hand[0].append(card)
        dealer_hand[1].append(deck[1][card_index])
        deck[0].remove(card)
        deck[1].remove(deck[1][card_index])
    
    # Showing player hand
    print("Player Hand:")
    for rank, suit in player_hand[0]:  
        print(rank, suit)
    # Showing dealer hand(only one card is shown)
    print("Dealer Hand:")
    for rank, suit in dealer_hand[0][:-1]:  
        print(rank, suit)
    print("# #")

    # Showing in the window the player hand
    show_cards_window(player_hand[1][0], 'left')
    show_cards_window(player_hand[1][1], 'left')
    # Showing in the window the dealer hand(only shows one card)
    show_cards_window(dealer_hand[1][0], 'right')
    card_back_label = show_cards_window(r"C:\Users\matth\Desktop\PNG-cards-1.3\card back black.png", 'right')
    # Saving index of hidden card
    dealer_hidden_card_index = len(card_labels) - 1

    # Adding up both the player and the dealers count
    player_count = calculate_counts(player_hand)
    dealer_count = calculate_counts(dealer_hand)
    
    # Checking for player Blackjack
    if player_count == 21:
        stand()

def calculate_counts(hand):
    # Sets total equal to zero
    total = 0
    aces = 0
    
    for card in hand[0]:
        rank = card[0]
        # If face card, value equals 10
        if rank in ['J', 'Q', 'K']:
            total += 10
        # If ace, count it separately
        elif rank == 'A':
            total += 11
            aces += 1
        else:
        # Adds all other values
            total += rank
    
    # Adjust for aces if total is over 21
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
        
    return total

def hit():
    global player_hand, player_count, player_balance, player_bet
    
    # Checks if deck is empty
    if len(deck[0]) < 1:
        update_message("Shute is over")
        print("No more cards in the deck.")
        return

    # Adds another random card to the players hand and shows it in the window
    card_index = random.randrange(len(deck[0]))
    card = deck[0][card_index]
    image_path = deck[1][card_index]

    player_hand[0].append(card)
    player_hand[1].append(image_path)

    deck[0].remove(card)
    deck[1].remove(image_path)

    show_cards_window(image_path, 'left')

    # Calculates the new player count
    player_count = calculate_counts(player_hand)
    print("Player count:", player_count)
    
    # If player count is over 21, the player busts and loses
    if player_count > 21:
        player_balance -= player_bet
        update_balance("Balance: $" + str(player_balance))
        reveal_dealer_hand()
        calc_dealer_count()
        print("Bust, Dealer Wins")
        update_message("Bust")
        # Disables both stand, hit, and double down buttons but enables the deal button
        hit_button.config(state="disabled")
        stand_button.config(state="disabled")
        double_down_button.config(state="disabled")
        deal_button.config(state="normal")
        # Resets the players bet
        player_bet = 0
        update_bet("Bet: $" + str(player_bet))
        # Resets chip buttons 
        red_chip_button.config(state="normal")
        green_chip_button.config(state="normal")
        blue_chip_button.config(state="normal")
        yellow_chip_button.config(state="normal")

def stand():
    global player_balance, player_bet, player_count
    
    print("Player balance:", player_balance)
    print("Player bet:", player_bet)
    # Disables the hit, stand, and double down buttons
    hit_button.config(state="disabled")
    stand_button.config(state="disabled")
    double_down_button.config(state="disabled")
    
    # Checking for Blackjack
    if player_count == 21 and len(player_hand[0]) == 2:
        update_message("Blackjack")
        player_balance += round(player_bet * 1.5)
    else:
        # Shows the dealers hidden card and their new count
        reveal_dealer_hand()
        calc_dealer_count()
        # Goes through basic outcomes, whether you or the dealer wins
        if dealer_count > 21:
            # Updating the players balance
            player_balance += player_bet
            update_balance("Balance: $" + str(player_balance))
            update_message("Dealer Bust, Win")
        elif player_count > dealer_count:
            # Updating the players balance
            player_balance += player_bet
            update_balance("Balance: $" + str(player_balance))
            update_message("Win")
            print("You win")
        elif player_count < dealer_count:
            # Updating the players balance
            player_balance -= player_bet
            update_balance("Balance: $" + str(player_balance))
            update_message("Dealer Wins")
            print("You lose")
        else:
            update_message("Push")
            print("push")
    
    # Resets the deal button
    deal_button.config(state="normal")
    # Resets the players bet
    player_bet = 0
    update_bet("Bet: $" + str(player_bet))
    # Resets chip buttons 
    red_chip_button.config(state="normal")
    green_chip_button.config(state="normal")
    blue_chip_button.config(state="normal")
    yellow_chip_button.config(state="normal")

def show_cards_window(image_path, side, steps=15, delay=30):
    # Load and resize the image
    pil_image = Image.open(image_path).resize((100, 145))
    enhancer = ImageEnhance.Brightness(pil_image)

    # Create a label 
    img = ImageTk.PhotoImage(enhancer.enhance(0))
    label = tk.Label(window, image=img, bg="green")
    label.image = img
    label.pack(side=side, padx=10, pady=10)
    card_labels.append(label)

    # Animation loop
    def animate(step=0):
        if step > steps:
            return
        bright_img = ImageTk.PhotoImage(enhancer.enhance(step / steps))
        label.configure(image=bright_img)
        label.image = bright_img
        window.after(delay, animate, step + 1)

    animate()

def show_buttons():
    global deal_button, hit_button, stand_button, shuffle_button, double_down_button
    
    # Function to show all the different buttons
    button_frame = tk.Frame(window, bg="green")
    button_frame.pack(pady=20)
    
    # Deal Button
    deal_button = tk.Button(button_frame, text="Deal", font=('Times New Roman', 20), command=deal_cards, bg="grey", fg="black")
    deal_button.pack(side="left", padx=10)
    
    # Hit button
    hit_button = tk.Button(button_frame, text="Hit", font=('Times New Roman', 20), command=hit, bg="grey", fg="black")
    hit_button.pack(side="left", padx=10)
    hit_button.config(state="disabled")
    
    # Stand button
    stand_button = tk.Button(button_frame, text="Stand", font=('Times New Roman', 20), command=stand, bg="grey", fg="black")
    stand_button.pack(side="left", padx=10)
    stand_button.config(state="disabled")
    
    # Shuffle button
    shuffle_button = tk.Button(button_frame, text="Shuffle Deck", font=('Times New Roman', 20), command=shuffle_cards, bg="grey", fg="black")
    shuffle_button.pack(side="left", padx=10)
    
    # Double down button
    double_down_button = tk.Button(button_frame, text="Double Down", font=('Times New Roman', 20), command=double_down, bg="grey", fg="black")
    double_down_button.pack(side="left", padx=10)
    double_down_button.config(state="disabled")

def show_chip_buttons():
    global red_chip_button, green_chip_button, blue_chip_button, yellow_chip_button, clear_bet_button
    
    # Function to show all the chips as buttons
    # Creates frame for the chip buttons
    chip_frame = tk.Frame(window, bg="green")
    chip_frame.pack(side="bottom", anchor="se", padx=20, pady=20)
    
    # Array for all chip photos
    chip_photos = []
    
    # Adds red chip
    image = Image.open(casino_chip_images[0])
    image = image.resize((100, 100)) 
    photo = ImageTk.PhotoImage(image)
    chip_photos.append(photo)  
    
    # Adds red chip image
    red_chip_button = tk.Button(chip_frame, text="$5", font=('Times New Roman', 30), compound="center", 
                              image=photo, bg="green", borderwidth=0, command=red_chip, fg="black")
    red_chip_button.image = photo
    red_chip_button.pack(side="left", padx=10)

    # Adds green chip
    image = Image.open(casino_chip_images[1])
    image = image.resize((100, 100)) 
    photo = ImageTk.PhotoImage(image)
    chip_photos.append(photo)  
    
    # Adds green chip image
    green_chip_button = tk.Button(chip_frame, text="$10", font=('Times New Roman', 30), compound="center", 
                                image=photo, bg="green", borderwidth=0, command=green_chip)
    green_chip_button.image = photo
    green_chip_button.pack(side="left", padx=10)

    # Adds blue chip
    image = Image.open(casino_chip_images[2])
    image = image.resize((100, 100)) 
    photo = ImageTk.PhotoImage(image)
    chip_photos.append(photo)  
    
    # Adds blue chip image
    blue_chip_button = tk.Button(chip_frame, text="$25", font=('Times New Roman', 30), compound="center", 
                               image=photo, bg="green", borderwidth=0, command=blue_chip)
    blue_chip_button.image = photo
    blue_chip_button.pack(side="left", padx=10)

    # Adds yellow chip
    image = Image.open(casino_chip_images[3])
    image = image.resize((100, 100)) 
    photo = ImageTk.PhotoImage(image)
    chip_photos.append(photo)  
    
    # Adds yellow chip image
    yellow_chip_button = tk.Button(chip_frame, text="$100", font=('Times New Roman', 30), compound="center", 
                                 image=photo, bg="green", borderwidth=0, command=yellow_chip)
    yellow_chip_button.image = photo
    yellow_chip_button.pack(side="left", padx=10)

    # Clear bet button
    clear_bet_button = tk.Button(chip_frame, text="Clear Bet", font=('Times New Roman', 20), 
                               command=clear_bet, bg="grey", fg="black")
    clear_bet_button.pack(side="left", padx=10)

def update_message(text):
    # Function to change the message output in the window
    message_label.config(text=text)

def update_balance(text):
    # Function to change the balance output in the window
    balance_label.config(text=text)

def update_bet(text):
    # Function to change the bet output in the window
    bet_label.config(text=text)

def clear_card_images():
    # Clears all card images on screen
    for label in card_labels:
        label.destroy()
    card_labels.clear()

def calc_dealer_count():
    global dealer_count, dealer_hand
    
    # Calculates dealer count
    dealer_count = calculate_counts(dealer_hand)
    # Continues to add card to the dealers hand until he either busts or reaches 17
    while dealer_count < 17:
        if len(deck[0]) == 0:
            print("No more cards in the deck.")
            break

        # Draws and shows one card
        card_index = random.randrange(len(deck[0]))
        card = deck[0][card_index]
        image_path = deck[1][card_index]

        dealer_hand[0].append(card)
        dealer_hand[1].append(image_path)

        deck[0].remove(card)
        deck[1].remove(image_path)

        show_cards_window(image_path, 'right')

        # Recalculates the dealers count
        dealer_count = calculate_counts(dealer_hand)
        print("Dealer draws:", card)
        print("Dealer total:", dealer_count)
    
    # Checks if the dealer busts
    if dealer_count > 21:
        print("Dealer busts")
    else:
        print("Dealer stands")

def reveal_dealer_hand():
    global dealer_hidden_card_index
    
    # Gets rid of the dealers hidden card image and removes it from card labels
    if dealer_hidden_card_index is not None and dealer_hidden_card_index < len(card_labels):
        card_labels[dealer_hidden_card_index].destroy()
        card_labels.pop(dealer_hidden_card_index)

        # Inserts the actual card at that card position
        second_card_path = dealer_hand[1][1]
        image_path = second_card_path
        pil_image = Image.open(image_path)
        pil_image = pil_image.resize((100, 145))
        img = ImageTk.PhotoImage(pil_image)
        label = tk.Label(window, image=img)
        label.image = img
        label.pack(side='right', padx=10, pady=10)
        card_labels.insert(dealer_hidden_card_index, label)
        # Resets the location of the dealers hidden card
        dealer_hidden_card_index = None 

def red_chip():
    global player_bet, player_balance
    # Adds 5 to the players bet
    if player_bet <= player_balance - 5:
        player_bet += 5
        update_bet("Bet: $" + str(player_bet))

def green_chip():
    global player_bet, player_balance
    # Adds 10 to the players bet
    if player_bet <= player_balance - 10:
        player_bet += 10
        update_bet("Bet: $" + str(player_bet))

def blue_chip():
    global player_bet, player_balance
    # Adds 25 to the players bet
    if player_bet <= player_balance - 25:
        player_bet += 25
        update_bet("Bet: $" + str(player_bet))

def yellow_chip():
    global player_bet, player_balance
    # Adds 100 to the players bet
    if player_bet <= player_balance - 100:
        player_bet += 100
        update_bet("Bet: $" + str(player_bet))

def double_down():
    global player_bet, player_balance
    # Doubles the players bet
    if player_bet <= player_balance - player_bet:
        player_bet *= 2
        update_bet("Bet: $" + str(player_bet))
    
    double_down_button.config(state="disabled")
    # Adds another random card to the players hand and shows it in the window
    card_index = random.randrange(len(deck[0]))
    card = deck[0][card_index]
    image_path = deck[1][card_index]

    player_hand[0].append(card)
    player_hand[1].append(image_path)

    deck[0].remove(card)
    deck[1].remove(image_path)

    show_cards_window(image_path, 'left')

    # Calculates the new player count
    player_count = calculate_counts(player_hand)
    print("Player count after double down:", player_count)

    # Calls the stand() function
    stand()
   
def clear_bet():
    global player_bet
    player_bet = 0
    update_bet("Bet: $" + str(player_bet))

setup_window()
    





    

