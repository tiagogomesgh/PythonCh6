### Tiago Gomes - 2375703
### COP1000 - #1284
### Program6_2.py

### Pseudocode
### Open lpsale.txt in read mode
### read album_title before while loop begins
### Create a while loop that runs unless album_title is empty
### Strip new line from album_title
### Read artist name, price, and discount %.
### Convert price and discount back to respective, float and integer.
### calculate the discount total, and discounted price.
### print each variable under column headings.
### Continue the loop until the album title is empty.

def main ():
    ### Opens file in read mode.
    file = open('lpsale.txt','r')
    
    ### Prints column headings before the loop begins.
    print(f'{"Album Title":<20}{"Arist(s) Name(s)":>15}{"Discount ($)":^15}{"Total Price after Discount ($)":>15}')
    print("---------------------------------------------------------------------------------")
    
    ### Reads album title from file
    album_title = file.readline()

    while album_title != '' :

        ### Strips New Line
        album_title = album_title.rstrip('\n')
        ### Reads artist name from file & strips new line.
        artist_name = file.readline()
        artist_name = artist_name.rstrip('\n')
        
        ### reads price from file and converts back to float.
        price = float(file.readline())
        
        ### reads discount and converts back to int.
        discount = int(file.readline())

        ### Calculates discount $ and total price after discount.
        discountedPrice = price * discount / 100
        totalPrice = price - discountedPrice
        
        ### Fills each Column.
        print(f'{album_title:<20}{artist_name:>15}{discountedPrice:^15.2f}{totalPrice:>15.2f}')
        
        ### Continues the loop until the album_title is empty.
        album_title = file.readline()



if __name__ == "__main__":
   main()
