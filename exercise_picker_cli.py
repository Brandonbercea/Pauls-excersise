import json
import random
import argparse

diastasis_recti_exercises = {
    "Level 1": {
        "Lying": [
            {
                "name": "Bent Knee Dead Bug",
                "page": 5,
                "notes": "Lie on your back, knees at 90 degrees, alternate arm and leg extensions while maintaining core bracing."
            },
            {
                "name": "Lying Knee Drops (Straight Knee)",
                "page": 5,
                "notes": "Start lying with knees bent, extend one leg, lower towards floor, keep back flat."
            },
            {
                "name": "Lying Single Leg Lifts (Straight Knee)",
                "page": 6,
                "notes": "Flat on back, one leg extended, lift leg to 45 degrees, keep core engaged."
            }
        ],
        "Side": [
            {
                "name": "Modified Side Plank",
                "page": 11,
                "notes": "Begin in a side plank with knees bent, focus on core endurance."
            },
            {
                "name": "Side-Lying Hip Abduction",
                "page": 11,
                "notes": "From a modified side plank, raise your top leg while engaging your core."
            },
            {
                "name": "Side-Lying Hip Adduction",
                "page": 12,
                "notes": "Similar to hip abductions, but focus on the lower leg raising."
            }
        ],
        "Standing": [
            {
                "name": "Standing Ball Squeezes",
                "page": 4,
                "notes": "Stand tall, brace your core, and squeeze a ball between your knees."
            },
            {
                "name": "Tree Pose",
                "page": 4,
                "notes": "Balance exercise, place one foot against opposite knee, raise arms overhead for difficulty."
            },
            {
                "name": "Wall Sit",
                "page": 4,
                "notes": "Lean against a wall, slide into a squat position, hold while engaging your core."
            }
        ]
    },
    "Level 2": {
        "Lying": [
            {
                "name": "Glute Bridge",
                "page": 14,
                "notes": "Lie on your back, squeeze your glutes to raise hips, hold at the top for 3 seconds."
            },
            {
                "name": "Dead Bug",
                "page": 16,
                "notes": "Perform pelvic tilt, then extend opposite arm and leg while keeping core tight."
            },
            {
                "name": "Lying Windshield Wiper",
                "page": 7,
                "notes": "Lie with knees bent, rotate legs side to side while keeping upper body stable."
            }
        ],
        "Side": [
            {
                "name": "Side Plank",
                "page": 12,
                "notes": "Hold a side plank position with legs extended, focus on core stability."
            },
            {
                "name": "Side Plank Dips",
                "page": 11,
                "notes": "Pulse hips up and down in a controlled manner while in side plank."
            },
            {
                "name": "Side Plank Rotations",
                "page": 11,
                "notes": "From a side plank, rotate torso and reach your arm underneath."
            }
        ],
        "Standing": [
            {
                "name": "Split Stance One Arm Shoulder Press",
                "page": 18,
                "notes": "In a split stance, press a dumbbell overhead, keeping your core tight."
            },
            {
                "name": "Pallof Press",
                "page": 14,
                "notes": "Use a resistance band to press forward while preventing rotation."
            },
            {
                "name": "Farmer Carry",
                "page": 14,
                "notes": "Hold a heavy object in one hand and walk, focusing on staying upright."
            },
            {
                "name": "Waiter Carry",
                "page": 14,
                "notes": "Hold a weight overhead in one hand and walk while keeping core engaged."
            }
        ]
    },
    "Level 3": {
        "Lying": [
            {
                "name": "Penguins",
                "page": 7,
                "notes": "Lie on your back, bend side-to-side to touch your heels, focusing on obliques."
            },
            {
                "name": "Lying Windshield Wiper with Knees Bent",
                "page": 7,
                "notes": "From the hollow body hold position, rotate bent knees side to side without letting them touch the ground."
            }
        ],
        "Side": [
            {
                "name": "Full Side Plank",
                "page": 12,
                "notes": "Hold the side plank with legs extended, focusing on full-body tension."
            },
            {
                "name": "Incline Side Plank",
                "page": 12,
                "notes": "Use a chair or bench for an easier side plank, holding for 10-15 seconds."
            }
        ],
        "Standing": [
            {
                "name": "Incline Push-Up Shoulder Tap",
                "page": 19,
                "notes": "Perform a push-up on an incline, then tap opposite shoulder while keeping your core engaged."
            },
            {
                "name": "Wall Plank",
                "page": 19,
                "notes": "Assume a plank position against a wall and hold for time."
            },
            {
                "name": "Standing Bicycles",
                "page": 5,
                "notes": "Stand tall, bring one knee toward opposite elbow while keeping your balance."
            }
        ]
    }
}

def info(excercise_list, human_readable=True):
    if human_readable:
        # Print the excercise name organized by level 
        for level, categories in excercise_list.items():
            print(f"{level} Exercises:")
            for category, exercises in categories.items():
                print(f"  {category} Exercises:")
            for exercise in exercises:
                print(f"    - {exercise['name']}")
        print("\n")
    else:
        # Print the full data structure in formatted json
        print(json.dumps(excercise_list, indent=4))




def pick_random_exercise(excercise_list, number_of_l1=3, number_of_l2=1, number_of_l3=0):
    if number_of_l1 is None:
        number_of_l1 = 0
    if number_of_l2 is None:
        number_of_l2 = 0
    if number_of_l3 is None:
        number_of_l3 = 0

    print("Picking random exercise...")

    # Ensure inputs are integers
    number_of_l1 = int(number_of_l1)
    number_of_l2 = int(number_of_l2)
    number_of_l3 = int(number_of_l3)

    # Initialize empty lists to store selected exercises
    level_1_exercises = []
    level_2_exercises = []
    level_3_exercises = []


    level_1_pool = []
    for category in excercise_list["Level 1"].values():
        level_1_pool.extend(category)

    level_1_exercises = random.sample(level_1_pool, min(len(level_1_pool), number_of_l1))

    level_2_pool = []
    for category in excercise_list["Level 2"].values():
        level_2_pool.extend(category)

    level_2_exercises = random.sample(level_2_pool, min(len(level_2_pool), number_of_l2))

    level_3_pool = []
    for category in excercise_list["Level 3"].values():
        level_3_pool.extend(category)
    level_3_exercises = random.sample(level_3_pool, min(len(level_3_pool), number_of_l3))

    # Combine all the selected exercises into a single list
    selected_exercises = {
     "l1": level_1_exercises, 
     "l2": level_2_exercises,
     "l3": level_3_exercises
    }

    # Print the selected exercises with headings of each level 
    print("Selected exercises:")

    print("\n Level 1:")
    for exercise in level_1_exercises:
        print(f"  - {exercise['name']}")
    print("\n Level 2:")
    for exercise in level_2_exercises:
        print(f"  - {exercise['name']}")
    if level_3_exercises:
        print("\n Level 3:")
        for exercise in level_3_exercises:
            print(f"  - {exercise['name']}")
    print("\n\n")

    # Return the selected exercises
    return selected_exercises




# Example usage:
# random_exercises = pick_random_exercise(diastasis_recti_exercises, number_of_l1=1, number_of_l2=1, number_of_l3=1)
# print(f"Randomly selected exercises: {random_exercises}")


# I want to take input from the command line with arguments for the number of excercises for each level and then return a random exercise plan for the day 
# I want to be able to call this from the terminal and get a different result each time

    

def main():
    parser = argparse.ArgumentParser(description="Pick a random exercise from the diastasis recti exercise list.")
    
    parser.add_argument("L1", type=str, help="The level of the exercise to pick from.")
    parser.add_argument("L2", type=str, help="The level of the exercise to pick from.")
    parser.add_argument("L3", type=str, help="The level of the exercise to pick from.")
    
    args = parser.parse_args()
    print(f"args: {args}")

    # Call the pick_random_exercise function with the provided arguments
    random_exercises = pick_random_exercise(diastasis_recti_exercises, args.L1, args.L2, args.L3)

    json_output = json.dumps(random_exercises, indent=4)
    print(json_output)

    return json_output

if __name__ == "__main__":
    main()

# Show me how to run this from the terminal
# python ./exercise_picker_cli.py 3 1 0
