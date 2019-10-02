
echo "Create data for Figure 1..."
matlab -nodisplay -nosplash -nodesktop -nojvm -r "run('figure1a.m');exit;" | tail -n +11
matlab -nodisplay -nosplash -nodesktop -nojvm -r "run('figure1c.m');exit;" | tail -n +11
matlab -nodisplay -nosplash -nodesktop -nojvm -r "run('figure1e.m');exit;" | tail -n +11
echo "Figure 1 done."

echo "Create data for Figure 2..."
matlab -nodisplay -nosplash -nodesktop -nojvm -r "run('figure2.m');exit;" | tail -n +11
echo "Figure 2 done."

echo "Create data for Figure 3..."
matlab -nodisplay -nosplash -nodesktop -nojvm -r "run('figure3.m');exit;" | tail -n +11
echo "Figure 3 done."

echo "Create data for Figure 4..."
matlab -nodisplay -nosplash -nodesktop -nojvm -r "run('figure4.m');exit;" | tail -n +11
echo "Figure 4 done."

echo "Create data for Figure 5..."
matlab -nodisplay -nosplash -nodesktop -nojvm -r "run('figure5.m');exit;" | tail -n +11
echo "Figure 5 done."

echo "Create data for Figure 6..."
matlab -nodisplay -nosplash -nodesktop -nojvm -r "run('figure6.m');exit;" | tail -n +11
echo "Figure 6 done."

echo "Create data for Figure 7..."
python3 figure7_I.py
matlab -nodisplay -nosplash -nodesktop -nojvm -r "run('figure7_II.m');exit;" | tail -n +11
echo "Figure 7 done."

echo "Create data for Figure 8..."
python3 figure8_I.py
matlab -nodisplay -nosplash -nodesktop -nojvm -r "run('figure8_II.m');exit;" | tail -n +11
echo "Figure 8 done."

echo "Create data for Figure 9..."
matlab -nodisplay -nosplash -nodesktop -nojvm -r "run('figure9.m');exit;" | tail -n +11
echo "Figure 9 done."
