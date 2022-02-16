'''
You are given a list of projects and a list of dependencies (which is a list
of pairs of projects, where the second project is dependent on the first project).
All of a project's dependencies must be built before the project is. Find a
builder order that will allow the projects to be built. If there is no
valid build order, return an error
'''
def is_build_finished(build_status):
    for project in build_status:
        if not build_status[project]:
            return False
    return True

def build_dependency_graph(projects, dependencies):
    dependency_graph = {}
    for p in projects:
        project_dependencies = [i for (i, j) in filter(lambda x: x[1] == p, dependencies)]
        dependency_graph[p] = project_dependencies
    return dependency_graph

def can_build(project, dependencies, build_status):
    for dep in dependencies:
        if not build_status[dep]:
            return False
    return True


def solution(projects, dependencies):
    project_dependencies = build_dependency_graph(projects, dependencies)
    build_status = { p: False for p in projects }
    built_project_during_cycle = True
    build_pipeline = []
    while not is_build_finished(build_status) and built_project_during_cycle:
        built_project_during_cycle = False
        for project in build_status:
            if can_build(project, project_dependencies[project], build_status):
                build_pipeline.append(project)
                build_status[project] = True
                built_project_during_cycle = True

    if not is_build_finished(build_status):
        return []
    return build_pipeline

def main():
    for test_case in [
        (['A','B'], []),
        (['A','B'], [('A', 'B'), ('B', 'A')])
    ]:
        print(solution(test_case[0], test_case[1]))

if __name__ == "__main__":
    main()
