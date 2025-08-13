package main

import (
	"fmt"
	"strings"
)

func validWordAbbreviation(word string, abbr string) bool {
	wordIndex := 0
	abbrIndex := 0

	for abbrIndex < len(abbr) {
		// Check if the current character is a digit.
		if abbr[abbrIndex] >= '0' && abbr[abbrIndex] <= '9' {
			// Check if there's a leading zero. If there is, return False.
			if abbr[abbrIndex] == '0' {
				return false
			}
			num := 0

			for abbrIndex < len(abbr) && abbr[abbrIndex] >= '0' && abbr[abbrIndex] <= '9' {
				// handles case when there are consecutive digits like 'i18n'
				num = num*10 + int(abbr[abbrIndex]-'0')
				abbrIndex++
			}
			// Skip the number of characters in word as found in abbreviation.
			wordIndex += num
		} else {
			// Check if characters match, then increment the pointers. Otherwise return False.
			if wordIndex >= len(word) || word[wordIndex] != abbr[abbrIndex] {
				return false
			}
			wordIndex++
			abbrIndex++
		}
	}

	// Check if both indices have reached the end of their respective strings.
	return wordIndex == len(word) && abbrIndex == len(abbr)
}

func main() {
	words := []string{"a", "a", "abcdefghijklmnopqrst", "abcdefghijklmnopqrst", "word", "internationalization", "localization"}
	abbreviations := []string{"a", "b", "a18t", "a19t", "w0rd", "i18n", "l10n"}

	for i, word := range words {
		fmt.Printf("%d.\t word: '%s'\n", i+1, word)
		fmt.Printf("\t abbr: '%s'\n", abbreviations[i])
		fmt.Printf("\n\t Is '%s' a valid abbreviation for the word '%s'? %v\n", abbreviations[i], word, validWordAbbreviation(word, abbreviations[i]))
		fmt.Println(strings.Repeat("-", 100))
	}
}

// Time complexity:
// The time complexity of the solution above is O(n), where n is the length of the word string word. This is because the solution processes each character of word exactly once.
// Space complexity:
// The space complexity is O(1) because the algorithm uses constant extra space regardless of the input size.
