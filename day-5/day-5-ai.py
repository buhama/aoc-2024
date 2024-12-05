from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Optional

@dataclass
class Rule:
    first_number: int
    second_number: int

    @classmethod
    def from_string(cls, rule_str: str) -> 'Rule':
        first, second = map(int, rule_str.split('|'))
        return cls(first, second)

class PageSorter:
    def __init__(self, input_file: Path):
        self.rules: List[Rule] = []
        self.pages: List[List[int]] = []
        self._load_data(input_file)

    def _load_data(self, input_file: Path) -> None:
        """Load and parse input file data."""
        adding_rules = True
        
        for line in input_file.read_text().splitlines():
            if not line:
                adding_rules = False
                continue
                
            if adding_rules:
                self.rules.append(Rule.from_string(line))
            else:
                self.pages.append([int(x) for x in line.split(',')])

    @staticmethod
    def _find_number_position(number: int, page: List[int]) -> Optional[int]:
        """Find position of a number in a page, return None if not found."""
        try:
            return page.index(number)
        except ValueError:
            return None

    @staticmethod
    def _get_middle_number(page: List[int]) -> int:
        """Get the middle number from a page."""
        return page[len(page) // 2]

    def _fix_page(self, page: List[int], rule: Rule, positions: Tuple[int, int]) -> List[int]:
        """Apply a rule fix to a page."""
        first_pos, second_pos = positions
        new_page = page.copy()
        new_page.pop(first_pos)
        new_page.insert(second_pos, rule.first_number)
        return new_page

    def _apply_rules(self, page: List[int]) -> Tuple[bool, Optional[List[int]]]:
        """Apply rules to a page until no more rules can be applied."""
        current_page = page.copy()
        modified = False

        while True:
            rule_applied = False
            
            for rule in self.rules:
                first_pos = self._find_number_position(rule.first_number, current_page)
                second_pos = self._find_number_position(rule.second_number, current_page)

                if None in (first_pos, second_pos) or first_pos <= second_pos:
                    continue

                current_page = self._fix_page(current_page, rule, (first_pos, second_pos))
                modified = True
                rule_applied = True
                break

            if not rule_applied:
                break

        return not modified, current_page if modified else None

    def process_pages(self) -> Tuple[int, int]:
        """Process all pages and return original and fixed middle number sums."""
        original_sum = 0
        fixed_sum = 0

        for page in self.pages:
            is_valid, fixed_page = self._apply_rules(page)
            
            if is_valid:
                original_sum += self._get_middle_number(page)
            elif fixed_page:
                fixed_sum += self._get_middle_number(fixed_page)

        return original_sum, fixed_sum

def main():
    sorter = PageSorter(Path("input.txt"))
    original_sum, fixed_sum = sorter.process_pages()
    
    print(f'Total middle sum: {original_sum}')
    print(f'Total middle sum fixed: {fixed_sum}')

if __name__ == "__main__":
    main()