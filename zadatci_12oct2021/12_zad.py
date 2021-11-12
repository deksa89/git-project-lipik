#12. Nađite sva ponavljanja ‘stol’ u zadanom stringu zanemarujući velika i mala slova: „U kuhinji je stol. STOL je novi.”

rijec = "stol"
string = "U kuhinji je stol. STOL je novi.".lower()

broj = string.count(rijec)

print(broj)