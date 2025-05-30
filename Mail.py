import random
import string

# র্যান্ডম ওয়ার্ড লিস্ট (পরিবর্তনযোগ্য)
WORD_LIST = [
    "mistyfern", "sunbloom", "frostfox", "calmriver", "cloudwhale", "joypetal", "windglow", "silverbreeze", "amberbird", "softmist",
    "bravelynx", "cosyfern", "mistrise", "lightmeadow", "dashcub", "swanshine", "hushlynx", "petalshade", "goldray", "waveleaf",
    "bluestar", "berryglow", "warmgleam", "silentstream", "iceleaf", "lavendermoon", "owlshade", "autumnfox", "moonwhisper", "foxbubble",
    "glowfern", "nightgleam", "duskbear", "mangoburst", "ottergleam", "fernveil", "moondrift", "tinycub", "orangemist", "snowglow",
    "boldpanda", "duckshine", "tropicmist", "gleamwave", "stonefern", "quietlynx", "fernmoon", "planetmist", "chillbreeze", "bananablush",
    "sproutmist", "lazymeadow", "leafdream", "bamboowave", "honeysky", "moonmist", "leafspin", "fernpeace", "owlshine", "frostfern",
    "glowfox", "twilightwing", "mooncandle", "zebrashade", "brightsky", "skyhush", "petalwhisper", "hillfern", "mistpath", "harmonyshade",
    "lynxlight", "shadowglow", "windcrest", "drizzleshine", "nestwhirl", "otternap", "bloomtrail", "daywhisper", "brookfrost", "goldpeak",
    "seashadow", "owlbeam", "snowpond", "shadehill", "rosestep", "dusklight", "pathglow", "towerfox", "flashwave", "hushshore",
    "warmmeadow", "softlynx", "stonemist", "duckhaze", "skylilt", "musepeak", "honeyglen", "skyfox", "lilacdreamer", "hushowl"
]



EMAIL_DOMAIN = "azuretechtalk.net"

# র্যান্ডম ওয়ার্ড বেছে নেওয়া
def generate_random_word():
    return random.choice(WORD_LIST)

# র্যান্ডম ৪ ডিজিটের সংখ্যা জেনারেট
def generate_random_number():
    return str(random.randint(1000, 9999))

# র্যান্ডম ২-৩টি অক্ষরের সাফিক্স
def generate_random_suffix():
    return ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 3)))

# কাস্টম টেম্প ইমেইল তৈরির ফাংশন
def create_custom_temp_email():
    username = f"{generate_random_word()}{generate_random_suffix()}{generate_random_number()}"
    return f"{username}@{EMAIL_DOMAIN}"
