import fitgit

C = fitgit.Commit()
C.add_json_file('example1-upload/file1.json', {'file': 1})
C.add_json_file('example1-upload/file2.json', {'file': 2})
C.add_json_file('example1-upload/file3.json', {'file': 3})
C.push_to_github('scratchrealm/test-content', branch='main', message='example1')

print('https://github.com/scratchrealm/test-content/tree/main/example1-upload')