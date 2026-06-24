# =============================
# ITEM DATA
# =============================

ITEM_DATA = {
    "name": "Nebula Suit of Creative",
    "base_atk": 100,
    "base_cri": 1
}

# =============================
# GRADE DATA (FIXED)
# =============================

GRADE_DATA = {
    "D": {
        "cri_d_every": 2,
        "cri_d_bonus": 2,
        "cri_every": 3,
        "cri_bonus": 1,
        "atk_bonus": 1
    },

    "C": {
        "cri_d_every": 2,
        "cri_d_bonus": 3,
        "cri_every": 3,
        "cri_bonus": 2,
        "atk_bonus": 2
    },

    "B": {
        "cri_d_every": 3,
        "cri_d_bonus": 5,
        "cri_r_every": 4,
        "cri_r_bonus": 1,
        "p_atk_bonus": 1
    },

    "A": {
        "cri_d_every": 3,
        "cri_d_bonus": 7,
        "cri_r_every": 4,
        "cri_r_bonus": 1,
        "p_atk_bonus": 2
    }
}

# =============================
# INPUT
# =============================

refine = int(input("Refine: "))
grade = input("Grade: ").upper()

# =============================
# BASE STATS
# =============================

atk = ITEM_DATA["base_atk"]
cri = ITEM_DATA["base_cri"]
cri_r = 0
cri_d = 0
p_atk = 0

# =============================
# REFINE SYSTEM
# =============================

atk += (refine // 2) * 10

if refine >= 9:
    cri += 5

if refine >= 11:
    cri_d += 20

# =============================
# GRADE SYSTEM
# =============================

g = GRADE_DATA.get(grade)

if g is None:
    print("Invalid Grade")
    exit()

# D / C
if grade in ["D", "C"]:
    atk += (refine // 3) * g["atk_bonus"]
    cri += (refine // 3) * g["cri_bonus"]
    cri_d += (refine // 2) * g["cri_d_bonus"]

# B / A
if grade in ["B", "A"]:
    cri_d += (refine // 3) * g["cri_d_bonus"]
    cri_r += (refine // 4) * g["cri_r_bonus"]
    p_atk += (refine // 4) * g["p_atk_bonus"]

# =============================
# OUTPUT
# =============================

print("\n====================")
print(ITEM_DATA["name"])
print("====================")
print(f"Refine : {refine}")
print(f"Grade  : {grade}")
print("====================")
print(f"ATK    : {atk}")
print(f"CRI    : {cri}")
print(f"CRI_R  : {cri_r}")
print(f"CDMG   : {cri_d}%")
print(f"P_ATK  : {p_atk}")
print("====================")