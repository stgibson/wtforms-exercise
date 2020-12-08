from models import Pet, db
from app import app

db.drop_all()
db.create_all()

names = ("Woofly", "Porchetta", "Snargle")
species = ("dog", "porcupine", "cat")
photo_urls = (
    "https://cdn.pixabay.com/photo/2016/12/13/05/15/puppy-1903313_960_720.jpg",
    "https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_960_720.jpg",
    "https://cdn.pixabay.com/photo/2018/08/06/23/32/nature-3588682_960_720.jpg"
)
ages = (12, 22, 4)
notes = ("This is my dog", "beware of spikes", "cute")

pets = [Pet(name=pet[0], species=pet[1], photo_url=pet[2], age=pet[3], \
    notes=pet[4]) for pet in zip(names, species, photo_urls, ages, notes)]

db.session.add_all(pets)
db.session.commit()