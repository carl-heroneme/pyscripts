{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "\n",
    "rootdir = os.getcwd()\n",
    "henrystat = open(\"HenryStat.txt\", \"a\")\n",
    "henrystat.write(\"MPa\")\n",
    "\n",
    "for subdir, dirs, files in os.walk(rootdir):\n",
    "    for file in files:\n",
    "        if os.path.join(subdir,file).find(\"log\") != -1:\n",
    "            with open(os.path.join(subdir,file), \"r\") as out_file:\n",
    "                for line in out_file:\n",
    "                    if line.find(\"Henry Law (Residual)\") != -1:\n",
    "                        words = line.split()\n",
    "                        henry = words[5]\n",
    "            henrystat.write(str(henry)+\"\\n\")\n",
    "henrystat.close()\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
