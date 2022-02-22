# SOFTWARE ENGINEERING IMMERSIVE - PROJECT FOUR #

A Full Stack project as a team of four with a 1 week deadline.

### Collaborators ###
* [Alex Chan](https://github.com/achan81 "Alex Chan")
* [Alex Theoklitou](https://github.com/alextheoklitou "Alex Theoklitou")
* [Mike Salter](https://github.com/msalter91 "Mike Salter")

## PawHub ##
The final project on the SEI course. In a team of four we had 1 week to create a Full Stack app, the backend was built with Django and Python, the front end was React.js

![homepage](assets/readMe/homepage.png)

## Brief ##
* Build a full-stack application - by making your own backend and your own front-end.
* Use an Express API to serve your data from the Mongo database.
* Consume your API with a separate front-end built with React.
* Create a MERN app & ensure there is CRUD functionality. 
* Implement thoughtful user stories/wireframes that are significant enough to help you know which features are core MVP and which you can cut.
* Have a visually impressive design.
* Be deployed online so it's publicly accessible.

## Built With ##
* Frontend
  * React.js
  * JSX
  * CSS and Sass
  * Tailwind Framework
  * Axios
  * React Toast Notification
  * Hamburger-React
* Backend 
  * Python
  * Django
* Dev Tools
  * Git
  * GitHub
  * FireFox dev tools
  * VScode
  * Insomnia
  * TablePlus

  ## Deployment ##
The app is deployed on Netlify and can be found [**here**](https://pawhub.netlify.app "here").  
(Please open with Chrome, more on this later.)  


## Process ##
For this one week project we were given the opportunity to choose if we wanted to work in teams or work solo. The four of us decided we wanted to work together and our goal was to create the slickest and most polished app possible within our time limit. Being dog lovers we were enticed by the idea of cloning the dogs trust website. Dogs + Code = Happiness.

We created an ERD diagram and used this to visually display our model relationships in the backend. 

![wireframe](/assets/readMe/wireframe.png)

We also created a virtual whiteboard using Miro, this enabled us to collaborate on a shared space, add notes, create to-do lists and plan our days as a team. 

![miro](assets/readMe/miro.png)

## Work Split ##
Being in a team of four it was important we split the roles of Backend and Frontend evenly so everybody played a full stack role on this project. During the project we were in constant communication with one another on Zoom, we created our own Slack chat so we could send each other code and we scheduled daily team stand up sessions each morning so we could discuss any challenges, talk about wins, and plan the day ahead.
Backend was done as a team, but each member took the lead on separate occasions, see Backend section below.
For the front end, my primary focus was the Navbar and routing of the app and then I progressed onto the about us, who we are, and fundraiser pages. 
Alex C, covered the extensive form of the adopt a dog page & also the donate page.
Alex T, took on the index and show pages. 
Mike S, handled the homepage, newsletter & footer. 

## Backend ##
Covering the backend first, the developer which was coding would share their screen, allowing all the other team mates to watch as they coded their chosen section. Once each person had coded their part they would add, commit & push to a development branch, working this way allowed all members of the team to assist and guide each other when making the backend. My main focus was on creating the views for register and login as well as some authentication. 
```js
class UserRegisterView(CreateAPIView):
   ''' View for Users Registration /register POST'''
   queryset = User.objects.all()
   serializer_class = UserRegistrationSerializer
 
 
class UserLoginView(APIView):
   ''' View for Users Login /login POST'''
 
   def post(self, request):
       username = request.data.get('username')
       password = request.data.get('password')
 
       try:
           user_to_login = User.objects.get(username=username)
       except User.DoesNotExist:
           raise PermissionDenied({'detail':'Unauthorized'})
 
       if not user_to_login.check_password(password):
           raise PermissionDenied({'detail':'Unauthorized'})
 
       expiry_time = datetime.now() + timedelta(days=7)
 
       token = jwt.encode(
           {'sub': user_to_login.id, 'exp': int(expiry_time.strftime('%s'))},
           settings.SECRET_KEY,
           algorithm='HS256'
       )
 
       return Response({
           'token': token,
           'message': f'Welcome back {user_to_login.username}'
       })
```

Below is the code for the JWT authentication.
```js
class JWTAuthentication(BasicAuthentication):
 
   def authenticate(self, request):
       header = request.headers.get('Authorization')
 
       if not header:
           return None
 
       if not header.startswith('Bearer'):
           raise PermissionDenied({'detail':'Invalid Auth Header'})
 
       token = header.replace('Bearer ', '')
 
       try:
           payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
           user = User.objects.get(pk=payload.get('sub'))
       except jwt.exceptions.InvalidTokenError:
           raise PermissionDenied({'detail':'Invalid Token Error'})
       except User.DoesNotExist:
           raise PermissionDenied({'detail':'User Not Found'})
 
       return (user, token)
```

We also all individually spent time adding in a lot of dummy data to our seeds, this is so when you click onto the site there are plenty of dogs to choose from giving it a genuine feel.
Example: 
```js
 {
   "model": "dogs.dog",
   "pk": 1,
   "fields": {
     "name": "Boo",
     "breed": "Greyhound",
     "age": "5",
     "sex": "Female",
     "home_details": "Boo is looking for a nice quiet home where people will be around a lot of the time. She would love a garden to burn off some energy off in.",
     "about": "Boo loves nothing more than sleeping, eating sausages and going for brief walks. She is a small greyhound with a big personality. She is unphased by other dogs, but can be very watchful of other smaller animals.",
     "can_live_with_dogs": true,
     "can_live_with_cats": false,
     "can_live_with_kids": false,
     "date_added": "2022-01-22T16:45:53Z",
     "image_one": "https://imgur.com/RGu0g3W.jpg",
     "image_two": null,
     "image_three": null
   }
 },
```

## Frontend ##
Once the backend was completed and working within insomnia, we linked it to the frontend and started building. Again, we split out duties across the team, each choosing our own tasks, agreeing with what was decided and then cracking on. We all agreed something we really wanted was the site to be responsive across all screen sizes.

For the front end, I focused on creating the Navbar, set out the routes within the App.js file, the about us page, who we are page and fundraiser page. I also included toast notifications to the app when logging in, as I really like this feature. 

## Navbar ##
As I hadn’t yet taken a lead on building a navbar with conditional formatting I was excited to focus on this element of the build. I tried to mimic elements of the Dog’s Trust Navbar as best I could, while still allowing myself some creative freedom with how it responded with the page. 

Here is a snippet to show the conditional formatting, checking to see if a user is logged in.
```js
     <nav className="nav-toggle sticky top-0 h-24 bg-white/80 z-50">
       <div className="flex float-left mt-2 pl-24">
         <Link className="flex float-left" to="/">
           <img src={pawhubLogo} alt="logo" className="h-20 w-20"></img></Link>
       </div>
       <div className="flex float-right mt-8 text-lg items-center">
         <Link className="mx-2" to="/dogs">View Dogs</Link>
         <Link className="mx-2" to="/aboutus">About Us</Link>
         <Link className="mx-2" to="/donation">Donate Now</Link>
         <Link className="mx-2" to="/newsletter">Newsletter</Link>
         {isAuth ? (
           <>
             <Link className="mx-2" to={`/profile/${userId}`}>Profile</Link>
             <button
               className="shadow-xl bg-pawhub-yellow hover:bg-pawhub-yellow/50 text-pawhub-grey font-bold py-2 px-5 rounded mr-24"
               onClick={handleLogout}>
               Logout
             </button>
           </>
         ) : (
           <>
             <Link className="mx-2" to="/register">Register</Link>
             <Link className="mx-2 pr-24" to="/login">Login</Link>
           </>
         )}
       </div>
     </nav>
```

## Register / Login ##
Similarly to project Three, we really wanted the better UX of automatically being logged in when registering as a new user. This is achieved by setting the login data into state. 
```js
 const handleChange = (e) => {
   setFormData({ ...formData, [e.target.name]: e.target.value })
   setFormErrors({ ...formErrors, [e.target.name]: '' })
   setLoginData({ username: e.target.name === 'username' ? e.target.value : formData.username, password: e.target.name === 'password' ? e.target.value : formData.password })
 }
 
 const handleSubmit = async (e) => {
   e.preventDefault()
   try {
     await registerUser(formData)
     const res = await loginUser(loginData)
     setToken(res.data.token)
     navigate('/')
   } catch (err) {
     setFormErrors(err.response.data)
   }
 }
 ```

## Filtering Dogs ##
One of the most useful tools when on a website with a large index of cards to choose from. Our filtering system on PawHub enables the user to not only filter on an individual field, but they can also stack these together for an enhanced search. 
```js
const filteredDogs = (dogs) => {
   return dogs.filter(dog => {
     return (breed.includes(dog.breed) || breed.length === 0) &&
       (age.includes(dog.age) || age.length === 0) &&
       (dog.canLiveWithDogs && liveWith.includes('Dogs') || !liveWith.includes('Dogs')) &&
       (dog.canLiveWithCats && liveWith.includes('Cats') || !liveWith.includes('Cats')) &&
       (dog.canLiveWithKids && liveWith.includes('Children') || !liveWith.includes('Children'))
   })
 }
```

## Favouriting Dogs ##
Essential to creating your shortlist of favourite adorable dogs. This feature allows the user to see all their favourited dogs in one place.
After logging in, you will see a purple heart appear next on any selected dogs show page. Clicking the heart will add this dog to your favourites, which are accessible on the Profile page.
```js
 const handleFavorite = async () => {
   if (!isFavorited) {
     try {
       const res = await favoriteDog(dogId, favoriteObject)
       setIsFavorited(true)
       setFavoriteId(res.data.id)
     } catch (err) {
       console.log(err)
     }
   } else {
     try {
       await removeFavorite(dogId, favoriteId)
       setIsFavorited(false)
     } catch (err) {
       console.log(err)
     }
   }
 }
```

## Comments ## 
Seen a dog you like? Well then you should be able to write a comment on that specific dog for more information. We added in a comment section at the bottom of each dog show page.
```js
 const handleSubmit = async (e) => {
   e.preventDefault()
   try {
     await createQuestion(dogId, { content: question, dog: dogId, owner: userId })
     setQuestion('')
   } catch (err) {
     console.log(err)
   }
 }
```

## Donate, Rehoming a Dog and Newsletter ##
These are three separate pages, however they all make use of React forms. A tricky part for the team here was to figure out how to keep the ‘£’ within the custom donate field. 

![donate](/assets/readMe/donate.png)

## Error Handling ##
The error handling on PawHub is a nice feature, displaying what error you have accompanied by a picture of a dog to suit, with thanks to httpstatusdogs.com

![error](/assets/readMe/error.png)

```js
import { ErrorImages } from '../../assets/errors/data'
 
function Error({ error }) {
 
 return (
   <section className="flex justify-center bg-black text-white">
     <div className="flex flex-col w-2/3 items-center" >
      
       {error < 500 ?
         <h2 className="gooddog-font text-3xl pt-5">There seems to have been an error...</h2> :
         <h2 className="gooddog-font text-3xl pt-5">It&apos;s not you, it&apos;s us...</h2>
       }
       <img className="object-center" src={ErrorImages[0][error]} />
     </div>
   </section>
 )
}
```

## About Us, Who We Are, Fundraiser ##
Taking care of the about us page, the main thing here was to ensure the pages were visually clean and give a space for each of the developers working on this site to say give a bio about themselves. This is where I came to a few blocks with Tailwind and slowly worked out how to use the tool effectively.

![aboutus](/assets/readMe/aboutus.png)

![whoweare](/assets/readMe/whoweare.png)

![fundraiser](/assets/readMe/fundraiser.png)

## More Screenshots ##

![index](/assets/readMe/index.png)

![show](/assets/readMe/show.png)

![comments](/assets/readMe/comments.png)

![loading](/assets/readMe/loading.png)

![newsletter](/assets/readMe/newsletter.png)

![questionnaire](/assets/readMe/questionnaire.png)

## Challenges ##
* My first block arose when trying to work out how to have my Navbar & burger-menu react to the correct way responsively and without interfering with each other. At first I was puzzling myself, trying to figure out how to have both in the same nav section, then I took a break, went and grabbed a coffee, 3 chocolate hobnobs, sat downstairs and patted my dog. When I came back to my desk the answer was immediately obvious, create two separate nav sections and use media queries to dictate which nav element showed in accordance to the screen size. 
* Working with Tailwind for the first time, I got off to a pretty slow start and struggled along for a little while. Eventually things started to work a little smoother for me though (even if I was dreaming of the project-three MUI days). 


## Bugs ##
* Firefox doesn’t allow for the custom fonts to load, so Google Chrome is currently the preferred browser for viewing this app.
* The carousel features sometimes break, causing the images to be lost.


## Future Improvements ##
* Bug fixes.
* Create a “recommended for you” section, where the app finds dog’s similar to the users preferences and puts them forward.
* Create a “give a dog up” section. 

## Wins & Key Learnings ##
* This project further reinforced how important communication and collaboration is when working within a team. The teamwork was excellent and it made the week even more enjoyable.
* Stepping away and taking a break is sometimes the perfect remedy to overcoming a block. 
* The site is fully mobile responsive.
* Really pleased with how clean the app looks.
