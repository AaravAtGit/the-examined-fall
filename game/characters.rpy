# Characters
# The image= tag links each speaker to their sprite folder, so you can write
#   a happy "line"
# and Ren'Py will swap Aarav's sprite to "aarav happy" automatically.

define a   = Character("Aarav",  color="#f5b942", image="aarav")
define o   = Character("Oreek",  color="#6fc3ff", image="oreek")
define s   = Character("Shrey",  color="#9be37a", image="shrey")
define dsp = Character("DSP",    color="#ff7a7a", image="dsp")

# Shrey is only on a phone call in Act 1, so he gets a label instead of a sprite.
define s_call = Character("Shrey (on call)", color="#9be37a", what_italic=False)

# Group chat messages
define gc = Character("Haven GC", color="#aaaaaa", what_prefix="> ", what_color="#dddddd")

# Muffled voices heard from inside the suitcase
define o_muffled = Character("Oreek (muffled)", color="#6fc3ff", what_italic=True)

# Act 2
define ng  = Character("The Guy",   color="#c0c4cc", image="theguy")
define j   = Character("Jassi",     color="#ffb3d9", image="jassi")
define ed  = Character("Edvance",   color="#c9a7ff", image="edvance")

# Act 3: 3am. Shwetank, and philosophers who may or may not be caffeine-induced.
define shw   = Character("Shwetank",          color="#7ee0d0", image="shwetank")
define des   = Character("René Descartes",    color="#e8d9a8", image="descartes")
define dio   = Character("Diogenes",          color="#d9b382", image="diogenes")
define scho  = Character("Schopenhauer",      color="#9aa6c2", image="schopenhauer")
define cam   = Character("Camus",             color="#f0a07a", image="camus")
define kie   = Character("Kierkegaard",       color="#b7c99a", image="kierkegaard")
define everyone = Character("Everyone")
