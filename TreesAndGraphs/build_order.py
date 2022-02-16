'''
You are given a list of projects and a list of dependencies (which is a list
of pairs of projects, where the second project is dependent on the first project).
All of a project's dependencies must be built before the project is. Find a
builder order that will allow the projects to be built. If there is no
valid build order, return an error
'''
def build_dependencies(projects, dependencies):
    dependency_graph = {}
    for p in projects:
        project_dependencies = [i for (i, j) in filter(lambda x: x[1] == p, dependencies)]
        dependency_graph[p] = project_dependencies

def solution(projects, dependencies):
    dependency_graph = build_dependencies(projects, dependencies)
    build_status = { p: False for p in projects }

    dependency_list = [
        (project, dependency_graph[project])
        for project in dependency_graph
    ]
    print(dependency_list)
    dependency_list.sort(key=lambda pd: len(pd[1]))
    print(dependency_list)
    return False

def main():
    for test_case in [
        (['A','B'], []),
        (['A','B'], [('A', 'B')])
    ]:
        print(solution(test_case[0], test_case[1]))

if __name__ == "__main__":
    main()
