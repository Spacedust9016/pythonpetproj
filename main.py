"""
File Analyzer - Entry point
Run with: python main.py [--classic | --modern | --profile-card]
"""
import sys
import argparse


def run_classic():
    """Run the classic UI."""
    from gui import main
    main()


def run_modern():
    """Run the modern AI-like UI."""
    from modern_gui import main
    main()


def main():
    parser = argparse.ArgumentParser(description='File Analyzer - Visual Storage Explorer')
    parser.add_argument(
        '--classic', 
        action='store_true',
        help='Use the classic interface (original design)'
    )
    parser.add_argument(
        '--modern',
        action='store_true', 
        help='Use the modern AI-like interface (default)'
    )
    parser.add_argument(
        '--profile-card',
        action='store_true',
        help='Print a simple anime ASCII GitHub profile card and exit'
    )
    
    args = parser.parse_args()
    
    if args.profile_card:
        from github_profile_terminal import main as profile_main
        profile_main()
        return

    # Default to modern if no flag specified
    if args.classic:
        print("🎨 Starting File Analyzer with Classic UI...")
        run_classic()
    else:
        print("✨ Starting File Analyzer with Modern UI...")
        print("   (Use --classic flag for original interface)")
        try:
            run_modern()
        except ImportError as e:
            print(f"\n⚠️  Modern UI requires additional dependencies: {e}")
            print("   Falling back to Classic UI...\n")
            run_classic()


if __name__ == '__main__':
    main()
