import sys

from graph import Graph


def print_menu():
    print("\nGraph Operations:")
    print("1. Add vertex")
    print("2. Add edge")
    print("3. Remove edge")
    print("4. Show vertices")
    print("5. Show edges")
    print("6. Check path existence")
    print("7. Find path")
    print("8. Check if cyclic")
    print("0. Exit")


def main(non_interactive=False):
    graph = Graph()

    if non_interactive:
        # Demo mode: Create a sample graph
        print("Running in demo mode...")
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_edge("A", "B", 1.0)
        graph.add_edge("B", "C", 2.0)

        print("\nVertices:", graph.get_vertices())
        print("\nEdges:")
        for from_v, to_v, weight in graph.get_edges():
            print(f"  {from_v} -> {to_v} (weight: {weight})")

        print("\nPath from A to C:", " -> ".join(graph.find_path("A", "C")))
        print("Is cyclic:", graph.is_cyclic())
        return

    while True:
        print_menu()
        try:
            choice = input("\nEnter your choice (0-8): ")

            if choice == "0":
                print("Goodbye!")
                break

            elif choice == "1":
                vertex = input("Enter vertex name: ")
                graph.add_vertex(vertex)
                print(f"Vertex '{vertex}' added.")

            elif choice == "2":
                from_v = input("Enter source vertex: ")
                to_v = input("Enter destination vertex: ")
                weight = float(input("Enter edge weight (default=1.0): ") or 1.0)
                graph.add_edge(from_v, to_v, weight)
                print(f"Edge from '{from_v}' to '{to_v}' with weight {weight} added.")

            elif choice == "3":
                from_v = input("Enter source vertex: ")
                to_v = input("Enter destination vertex: ")
                graph.remove_edge(from_v, to_v)
                print(f"Edge from '{from_v}' to '{to_v}' removed.")

            elif choice == "4":
                vertices = graph.get_vertices()
                print("Vertices:", vertices)

            elif choice == "5":
                edges = graph.get_edges()
                print("Edges:")
                for from_v, to_v, weight in edges:
                    print(f"  {from_v} -> {to_v} (weight: {weight})")

            elif choice == "6":
                start = input("Enter start vertex: ")
                end = input("Enter end vertex: ")
                if graph.has_path(start, end):
                    print(f"Path exists from '{start}' to '{end}'")
                else:
                    print(f"No path exists from '{start}' to '{end}'")

            elif choice == "7":
                start = input("Enter start vertex: ")
                end = input("Enter end vertex: ")
                path = graph.find_path(start, end)
                if path:
                    print(f"Path found: {' -> '.join(str(v) for v in path)}")
                else:
                    print(f"No path exists from '{start}' to '{end}'")

            elif choice == "8":
                if graph.is_cyclic():
                    print("The graph contains cycles.")
                else:
                    print("The graph is acyclic.")

            else:
                print("Invalid choice!")

        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main("--demo" in sys.argv)

