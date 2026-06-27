
import config # load_dotenv
from langchain_core.messages import HumanMessage

def main() :
	query = input('요즘 어떤 주식에 관심이 있으신가요?\n >> ')
	initial_state = [HumanMessage(query)]

	for chunk in graph.stream(initial_state, stream_mode='values') :
		chunk['messages'][-1].pretty_print()

if __name__ == "__main__" :
	main()
