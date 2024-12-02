import language_tool_python


def check_grammar(text):
    
    tool = language_tool_python.LanguageTool('en-US')

    matches = tool.check(text)

    if matches:
        print(f"Found {len(matches)} potential issues:")
        for i, match in enumerate(matches, 1):
            print(f"\nIssue {i}:")
            print(f" - Mistake: {match.context}")
            print(
                f" - Suggestion: {', '.join(match.replacements) if match.replacements else 'No suggestion available'}")
            print(f" - Explanation: {match.message}")
    else:
        print("No grammar issues found!")


user_text = input("Enter the text you want to check: ")
check_grammar(user_text)
