import requests
import time
import json

HEAL_URL = "http://localhost:8000/locator/heal"

# ----------------------------------------------------------------------
# 20+ REALISTIC DOM TESTS
# ----------------------------------------------------------------------

tests = [
    # 1. Simple Move
    {
        "name": "Simple Move",
        "old": "<button id='signup'>Sign Up</button>",
        "new": "<section><button>Sign Up</button></section>",
        "expected": "Sign Up"
    },

    # 2. Text Change - Semantic
    {
        "name": "Semantic Change",
        "old": "<button id='signup'>Sign Up</button>",
        "new": "<button>Create Account</button>",
        "expected": "Create Account"
    },

    # 3. ID Removed
    {
        "name": "ID Removed",
        "old": "<button id='signup'>Sign Up</button>",
        "new": "<button class='primary'>Sign Up</button>",
        "expected": "Sign Up"
    },

    # 4. Structure Changed
    {
        "name": "Parent Structure Change",
        "old": "<div class='auth'><button id='signup'>Sign Up</button></div>",
        "new": "<div class='header'><button>Create Account</button></div>",
        "expected": "Create Account"
    },

    # 5. Deep Nesting
    {
        "name": "Deep Nesting",
        "old": "<button id='signup'>Sign Up</button>",
        "new": "<div><main><section><button>Sign Up</button></section></main></div>",
        "expected": "Sign Up"
    },

    # 6. Neighbor Driven
    {
        "name": "Neighbor Driven",
        "old": "<label>Name</label><button>Sign Up</button>",
        "new": "<div><h3>Name</h3><button>Create Account</button></div>",
        "expected": "Create Account"
    },

    # 7. Neighbor Missing
    {
        "name": "Neighbor Missing",
        "old": "<label>Name</label><button>Sign Up</button>",
        "new": "<button>Create Account</button>",
        "expected": "Create Account"
    },

    # 8. Dynamic ID
    {
        "name": "Dynamic ID",
        "old": "<button id='signup'>Sign Up</button>",
        "new": "<button id='btn-123-random'>Sign Up</button>",
        "expected": "Sign Up"
    },

    # 9. A/B Testing Variation
    {
        "name": "A/B Variation",
        "old": "<button>Sign Up</button>",
        "new": "<button>Join Now</button>",
        "expected": "Join Now"
    },

    # 10. Responsive Mobile Layout
    {
        "name": "Mobile Layout",
        "old": "<button>Sign Up</button>",
        "new": "<div class='mobile-cta'><button>Create Account</button></div>",
        "expected": "Create Account"
    },

    # 11. Icon Added Inside Button
    {
        "name": "Icon Added",
        "old": "<button>Sign Up</button>",
        "new": "<button><i></i>Sign Up</button>",
        "expected": "Sign Up"
    },

    # 12. Text Split Across Spans
    {
        "name": "Split Text",
        "old": "<button>Sign Up</button>",
        "new": "<button><span>Sign </span><span>Up</span></button>",
        "expected": "Sign Up"
    },

    # 13. Foreign Language
    {
        "name": "Internationalization (i18n)",
        "old": "<button>Sign Up</button>",
        "new": "<button>Registrieren</button>",
        "expected": "Registrieren"
    },

    # 14. ARIA Label
    {
        "name": "Accessibility Label",
        "old": "<button>Sign Up</button>",
        "new": "<button aria-label='Create account'></button>",
        "expected": "Create account"
    },

    # 15. Button -> Link
    {
        "name": "Button to Link",
        "old": "<button>Sign Up</button>",
        "new": "<a class='cta'>Sign Up</a>",
        "expected": "Sign Up"
    },

    # 16. Multiple Similar Buttons
    {
        "name": "Multiple Similar",
        "old": "<button>Sign Up</button>",
        "new": "<div><button>Sign Up</button><button>Sign Up Free</button></div>",
        "expected": "Sign Up"
    },

    # 17. Moved Into Modal
    {
        "name": "Moved to Modal",
        "old": "<button>Sign Up</button>",
        "new": "<div class='modal'><button>Create Account</button></div>",
        "expected": "Create Account"
    },

    # 18. Sidebar Move
    {
        "name": "Sidebar Move",
        "old": "<button>Sign Up</button>",
        "new": "<aside><nav><button>Sign Up</button></nav></aside>",
        "expected": "Sign Up"
    },

    # 19. Shadow DOM
    {
        "name": "Shadow DOM",
        "old": "<button>Sign Up</button>",
        "new": "<custom-auth><shadow-root><button>Create Account</button></shadow-root></custom-auth>",
        "expected": "Create Account"
    },

    # 20. Full UI Rewrite
    {
        "name": "Full Rewrite",
        "old": "<button>Sign Up</button>",
        "new": "<div class='page'><main><button>Continue</button></main></div>",
        "expected": "Continue"
    }
]


# ----------------------------------------------------------------------
# TEST HARNESS
# ----------------------------------------------------------------------

def run_test(test):
    payload = {
        "element_key": "signup_button",
        "failed_locator": "//*[@id='signup']",
        "new_dom": test["new"]
    }

    start = time.time()
    try:
        r = requests.post(HEAL_URL, json=payload)
        resp = r.json()
    except Exception as e:
        return False, 0, f"Error: {str(e)}"

    healed = resp.get("healed_locator", "").lower()
    print(r.json(),"\n")
    expected = test["expected"].lower()
    duration = round((time.time() - start) * 1000, 2)

    # Accuracy condition: healed locator should contain expected text
    is_correct = expected in healed
    time.sleep(10)

    return is_correct, duration, healed


# ----------------------------------------------------------------------
# RUN ALL TESTS
# ----------------------------------------------------------------------

correct = 0
results = []

print("\n========= ACCURACY TEST RESULTS =========\n")

for t in tests:
    ok, time_ms, healed = run_test(t)
    status = "PASS" if ok else "FAIL"
    results.append((t["name"], status, time_ms, healed))

    color = "\033[92m" if ok else "\033[91m"
    print(f"{color}{status}\033[0m | {t['name']} | {time_ms} ms")
    print(f"    Healed: {healed}")
    print(f"    Expected contains: {t['expected'].lower()}\n")

    if ok:
        correct += 1

total = len(tests)
acc = (correct / total) * 100

print("\n=========================================")
print(f"FINAL ACCURACY: {correct}/{total} = {acc:.2f}%")
print("=========================================\n")
