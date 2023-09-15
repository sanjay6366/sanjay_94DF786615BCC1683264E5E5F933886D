'''implement a class named player that representes a cricket player
the player should have method named play which should print"the player is palying."
create a two classes named batsman and blower from player.
override the play method() in each of the classes that the "batsman is batting" and "blower is blowing".
write a program to create an object for each of the classes and call paly method() in each of the objects.'''

class player:
  def play(self):
    print("The palyer is playing...")
class Batsman(player):
      def play(self):
        print("The batsman is batting!!!")
class Blower(player):
          def play(self):
            print("Blower is blowing!!!")

batsman=Batsman()
blower=Blower()
batsman.play()
blower.play()