# lecture_2

## 🚀 Mini-Profile Generator

### Description
A simple interactive Python script that collects basic user information and builds a small profile:

- Full name  
- Year of birth (used to calculate current age)  
- Hobbies (entered one-by-one until the user types `stop`)  
- Life stage category based on age (`Child`, `Teenager`, `Adult`)

---

### Profile output
After input collection the script constructs a dictionary with the following keys:

- `name` — full name  
- `age` — calculated age (based on `CURRENT_YEAR`)  
- `stage` — life stage category  
- `hobbies` — list of hobbies

The resulting profile is printed to the console in a concise, readable format.

---

### Notes
- Type hints are used (`List[str]`, `Dict[str, Any]`, etc.).  
- `CURRENT_YEAR` is a top-level constant; update it to change the age reference year.  
- The script is fully interactive and intended for console use.



