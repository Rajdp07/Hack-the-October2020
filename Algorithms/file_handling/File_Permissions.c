#include <errno.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>

int main(int argc, char **argv)
{
    if (argc <= 1)
    {
        return -1;
    }
    // Directory starts
    struct stat dire;
    int t = stat(argv[3], &dire);
    if (t < 0)
    {
        write(STDOUT_FILENO, "Error in accessing Directory", 28);
        write(STDOUT_FILENO, "\n", 1);
    }
    else
    {

        if (S_ISDIR(dire.st_mode))
        {
            write(STDOUT_FILENO, "Directory is created: Yes", 25);
            write(STDOUT_FILENO, "\n", 1);

            if (dire.st_mode & S_IRUSR)
            {
                write(STDOUT_FILENO, "User has read permissions on Directory: Yes", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            else
            {
                write(STDOUT_FILENO, "User has read permissions on Directory: No", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            if (dire.st_mode & S_IWUSR)
            {
                write(STDOUT_FILENO, "User has write permissions on Directory: Yes", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            else
            {
                write(STDOUT_FILENO, "User has write permissions on Directory: No", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            if (dire.st_mode & S_IXUSR)
            {
                write(STDOUT_FILENO, "User has execute permissions on Directory: Yes", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            else
            {
                write(STDOUT_FILENO, "User has execute permissions on Directory: No", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            if (dire.st_mode & S_IRGRP)
            {
                write(STDOUT_FILENO, "Group has read permissions on Directory: Yes", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            else
            {
                write(STDOUT_FILENO, "Group has read permissions on Directory: No", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            if (dire.st_mode & S_IWGRP)
            {
                write(STDOUT_FILENO, "Group has write permissions on Directory: Yes", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            else
            {
                write(STDOUT_FILENO, "Group has write permissions on Directory: No", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            if (dire.st_mode & S_IXGRP)
            {
                write(STDOUT_FILENO, "Group has execute permissions on Directory: Yes", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            else
            {
                write(STDOUT_FILENO, "Group has execute permissions on Directory: No", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            if (dire.st_mode & S_IROTH)
            {
                write(STDOUT_FILENO, "Others has read permissions on Directory: Yes", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            else
            {
                write(STDOUT_FILENO, "Others has read permissions on Directory: No", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            if (dire.st_mode & S_IWOTH)
            {
                write(STDOUT_FILENO, "Others has write permissions on Directory: Yes", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            else
            {
                write(STDOUT_FILENO, "Others has write permissions on Directory: No", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            if (dire.st_mode & S_IXOTH)
            {
                write(STDOUT_FILENO, "Others has execute permissions on Directory: Yes", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
            else
            {
                write(STDOUT_FILENO, "Others has execute permissions on Directory: No", 48);
                write(STDOUT_FILENO, "\n", 1);
            }
        }
        else
        {
            write(STDOUT_FILENO, "Directory is created: No", 25);
            write(STDOUT_FILENO, "\n", 1);
        }
    }
    // Directory ends
    // old file starts
    struct stat oldfile;
    int fd1 = stat(argv[2], &oldfile);
    if (fd1 < 0)
    {
        write(STDOUT_FILENO, "Error in accessing oldfile", 30);
        write(STDOUT_FILENO, "\n", 1);
    }
    else
    {
        if (oldfile.st_mode & S_IRUSR)
        {
            write(STDOUT_FILENO, "User has read permissions on oldfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "User has read permissions on oldfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (oldfile.st_mode & S_IWUSR)
        {
            write(STDOUT_FILENO, "User has write permissions on oldfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "User has write permissions on oldfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (oldfile.st_mode & S_IXUSR)
        {
            write(STDOUT_FILENO, "User has execute permissions on oldfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "User has execute permissions on oldfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (oldfile.st_mode & S_IRGRP)
        {
            write(STDOUT_FILENO, "Group has read permissions on oldfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "Group has read permissions on oldfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (oldfile.st_mode & S_IWGRP)
        {
            write(STDOUT_FILENO, "Group has write permissions on oldfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "Group has write permissions on oldfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (oldfile.st_mode & S_IXGRP)
        {
            write(STDOUT_FILENO, "Group has execute permissions on oldfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "Group has execute permissions on oldfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (oldfile.st_mode & S_IROTH)
        {
            write(STDOUT_FILENO, "Others has read permissions on oldfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "Others has read permissions on oldfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (oldfile.st_mode & S_IWOTH)
        {
            write(STDOUT_FILENO, "Others has write permissions on oldfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "Others has write permissions on oldfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (oldfile.st_mode & S_IXOTH)
        {
            write(STDOUT_FILENO, "Others has execute permissions on oldfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "Others has execute permissions on oldfile: No", 46);
            write(STDOUT_FILENO, "\n", 1);
        }
    }
    long int oldfilesize = oldfile.st_size;
    // oldfile ends
    // newfile starts
    struct stat newfile;
    int fd2 = stat(argv[1], &newfile);
    if (fd2 < 0)
    {
        write(STDOUT_FILENO, "Error in accessing newfile", 30);
        write(STDOUT_FILENO, "\n", 1);
    }
    else
    {
        long int newfilesize = newfile.st_size;
        if (oldfilesize != newfilesize)
        {
            write(STDOUT_FILENO, "Whether file contents are reversed in newfile: No", 50);
            write(STDOUT_FILENO, "\n", 1);
                }
        else
        {
            int old = open(argv[2], O_RDONLY);
            int new = open(argv[1], O_RDONLY);
            if (old < 0)
            {
                perror("r1");
            }
            if (new < 0)
            {
                perror("r1");
                return -1;
            }
            long int testsize = oldfilesize / 10000;
            long int chuck, flag = 0;
            if (testsize == 0)
            {
                chuck = 1;
            }
            else
            {
                chuck = testsize;
            }
            char a[chuck], b[chuck];
            long int filesize = oldfilesize;
            oldfilesize = ((oldfilesize - 1) / chuck) * chuck;
            newfilesize = ((newfilesize - 1) / chuck) * chuck;
            long int i = filesize - oldfilesize;
            lseek(old, oldfilesize, SEEK_SET);
            lseek(new, 0, SEEK_SET);
            while (1)
            {
                read(old, a, i);
                read(new, b, i);
                long int end = i - 1;
                for (long int begin = 0; begin < i; begin++)
                {
                    if (b[begin] != a[end])
                    {
                        flag = 1;
                        break;
                    }
                    end--;
                }
                if (lseek(fd1, 0, SEEK_CUR) - chuck - i < 0 || (flag == 1))
                {
                    break;
                }
                lseek(old, -chuck - i, SEEK_CUR);
                lseek(new, chuck + i, SEEK_CUR);
                i = chuck;
            }
            if (flag == 0)
            {
                write(STDOUT_FILENO, "Whether file contents are reversed in newfile: Yes", 50);
                write(STDOUT_FILENO, "\n", 1);
            }
            else
            {
                write(STDOUT_FILENO, "Whether file contents are reversed in newfile: No", 50);
                write(STDOUT_FILENO, "\n", 1);
            }
        }
        if (newfile.st_mode & S_IRUSR)
        {
            write(STDOUT_FILENO, "User has read permissions on newfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "User has read permissions on newfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (newfile.st_mode & S_IWUSR)
        {
            write(STDOUT_FILENO, "User has write permissions on newfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "User has write permissions on newfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (newfile.st_mode & S_IXUSR)
        {
            write(STDOUT_FILENO, "User has execute permissions on newfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "User has execute permissions on newfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (newfile.st_mode & S_IRGRP)
        {
            write(STDOUT_FILENO, "Group has read permissions on newfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "Group has read permissions on newfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (newfile.st_mode & S_IWGRP)
        {
            write(STDOUT_FILENO, "Group has write permissions on newfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "Group has write permissions on newfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (newfile.st_mode & S_IXGRP)
        {
            write(STDOUT_FILENO, "Group has execute permissions on newfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "Group has execute permissions on newfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (newfile.st_mode & S_IROTH)
        {
            write(STDOUT_FILENO, "Others has read permissions on newfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "Others has read permissions on newfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (newfile.st_mode & S_IWOTH)
        {
            write(STDOUT_FILENO, "Others has write permissions on newfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "Others has write permissions on newfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        if (newfile.st_mode & S_IXOTH)
        {
            write(STDOUT_FILENO, "Others has execute permissions on newfile: Yes", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
        else
        {
            write(STDOUT_FILENO, "Others has execute permissions on newfile: No", 48);
            write(STDOUT_FILENO, "\n", 1);
        }
    }

    return 0;
}