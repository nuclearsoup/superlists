from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

    @skip
    def test_cannot_add_empty_list_items(self):
        # Mistakenly enters blank object

        # Page refreshes telling her entry cannot be empty

        # Try again with test for item which now succeeds

        # Perversely do same again and receives similar warning on list page.

        # And she can correct by filling some test in
        self.fail('write me!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
