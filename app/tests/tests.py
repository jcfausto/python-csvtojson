from app.translator.tests.translatorTests import TranslatorTests
from pycsvtojsonTests import PycsvtojsonTests


def main():
	test1 = PycsvtojsonTests()
	test1.run()
	test2 = TranslatorTests()
	test2.run()

if __name__ == '__main__':
    main()