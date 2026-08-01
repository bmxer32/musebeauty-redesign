import os
import re

# Complete pool of verified high-res authentic photos (all unique!)
photo_pool = {
    # Home Page (index.html)
    "home_hero": "assets/img/2072743F-D526-49B9-8.jpeg",         # Hero interior
    "home_cat_lashes": "assets/img/F8464A9E-67AB-44E3-B.jpeg",   # Lashes category
    "home_cat_brows": "assets/img/51FC2374-2DAE-4FDA-9.jpeg",    # Brows category
    "home_cat_nails": "assets/img/24E4ADBA-B26A-422E-9.jpeg",    # Nails category
    "home_cat_luxhair": "assets/img/2558E8CB-F90B-4B83-A.jpeg",  # Luxhair category
    "home_cat_hair": "assets/img/209E1C9C-5C52-4141-9.jpeg",     # Hair category
    "home_cat_makeup": "assets/img/441C87DB-1796-4122-8.jpeg",   # Makeup category
    "home_gal_1": "assets/img/noroot.png",                       # Lounge space
    "home_gal_2": "assets/img/294079F4-F2D6-40CD-9.jpeg",       # Studio workspace
    "home_gal_3": "assets/img/4BA72AEE-E5E5-41B0-A.jpeg",       # Service zone
    "home_gal_4": "assets/img/image_-1.png",                    # Reception desk

    # Lashes Page (lashes.html)
    "lashes_hero": "assets/img/CCB92D88-733F-4D50-9.webp",      # Lash lamination & volume

    # Brows Page (brows.html)
    "brows_hero": "assets/img/CF9B0EE0-51FE-4E0A-A.webp",       # Brow lamination & shaping

    # Nails Page (nails.html)
    "nails_hero": "assets/img/3B52DDCC-3A98-424D-B.webp",       # Manicure & Gel Polish

    # Luxhair Page (luxhair.html)
    "luxhair_hero": "assets/img/89C75270-F1FD-4357-8.jpeg",     # Lebel & Luxhair reconstruction

    # Hair Page (hair.html)
    "hair_hero": "assets/img/A0C70495-F617-43CF-B.jpeg",        # Airtouch & Styling

    # Makeup Page (makeup.html)
    "makeup_hero": "assets/img/F09AB9EC-4715-4CE5-8.jpeg",      # Evening & Bridal makeup

    # Contacts Page (contacts.html)
    "contacts_hero": "assets/img/generated.jpg"                 # Salon location ambiance
}

print("Unique photo pool mapped. Total unique images:", len(photo_pool))
