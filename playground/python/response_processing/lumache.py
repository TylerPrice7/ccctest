"""
Dummy python folder to test sphinx workflow.
"""
def getRandomIngredients(kind=None):
  """
  Return a list of random ingredients as strings.

  :param kind: Optional "kind" of ingredients.
  :type kind: list[str] or None
  :raise lumache.InvalidKindError: If the kind is invalid.
  :return: The ingredients list.
  :rtype: list[str]
  """
  if kind:
    return kind
  return ["shells", "gorgonzola", "parsley"]

class InvalidKindError(Exception):
  """Raised if the kind is invalid."""
