### Tiago Gomes - 2375703
### COP1000 - #1284
### Program6_1.py

### Psuedocode
### Open the file lpsale.txt in write mode.
### Prompt the user to enter the Album title.
### Start the while loop unless the album title is empty.
### Prompt the user to enter the artist name, price, and discount.
### Write each variable to the file, converting each float and int to string.
### Continue the while loop unless the album title is empty.
### Print a message stating that the file has been created correctly.


def main () :

    file = open('lpsale.txt','w')
    
    album_title = str(input("Enter the album's title: "))

    while album_title != '' :
        artist_name = str(input("Enter the artist(s) name(s): "))
        price = float(input("Enter the regular price: "))
        discount = int(input("Enter the discount in percent: "))
            
        file.write(album_title + '\n')
        file.write(artist_name + '\n')
        file.write(str(price) + '\n')
        file.write(str(discount) + '\n')

        album_title = str(input("Enter the album's title: "))

    print("The LP sale data has been succesfully stored in lpsale.txt.")
    file.close()


if __name__ == "__main__":
   main()
