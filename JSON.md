# Piece Check - Text Editing Application
## JSON Format
### What is Received

When the respons from the API is received, it is received in a format known as JSON. This JSON Format is used everywhere, esecially when there is the use of communication between applicaions via API.

### How it is Formatted

You can think of the JSON format as a format with a parent and child in a form of hierarchy. A good analogy of this is when you look at family trees. An example of a file formatted using JSON - 

```JSON

Rudra {
  Config {
    Age = 12
    Gender = 'Male'
    Height = 165
    Weight = 45
  }
  Interests {
    Interest_1 = 'Science'
    Interest_2 = 'Computers'
    Interest_3 = 'Writing'
    Interest_4 = 'Sports'
  } 
  Hobbies {
    Computers {
      ComputerHobby_1 = 'Watching science videos'
      ComputerHobby_2 = 'Creating applications'
      ComputerHobby_3 = 'Creating documentations on Github'
    }
    Sports {
      SportHobby_1 = 'Playing Cricket'
      SportHobby_2 = 'Playing Tennis'
      SportHobby_3 = 'Playing Soccer'
      SportHobby_4 = 'Playing Footy'
    }
  }
}
```
