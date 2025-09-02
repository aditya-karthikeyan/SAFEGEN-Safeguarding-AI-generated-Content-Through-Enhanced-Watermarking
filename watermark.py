from typing import List, Set

def count_redlist_terms(text: str, redlist: Set[str], unique: bool = True) -> int:
    tokens = [t.strip(".,!?;:"'()[]{}").lower() for t in text.split()]
    if unique:
        return len(set(t for t in tokens if t in redlist))
    return sum(1 for t in tokens if t in redlist)
