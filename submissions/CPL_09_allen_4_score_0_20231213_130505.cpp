#include <cassert>
class Matrix{
	friend ostream & operator<<(ostream &,const Matrix &);
	friend Matrix operator*(double a,const Matrix &m);
	friend Matrix operator*(const Matrix &m,double a);
	friend Matrix operator+(const Matrix &m,const Matrix &n);
	friend Matrix operator* (const Matrix &m,const Matrix &n);
	friend Matrix transpose(Matrix &p);
	public:
		double ** array;
		Matrix(int);
		Matrix();
		~Matrix();
		static const int dim;
		double& operator() (const int nCol, const int nRow);
		
		Matrix& operator+= (const Matrix &n);
		Matrix& operator*= (const Matrix &n);
		Matrix& operator= (const Matrix &p);
		
};
Matrix::Matrix(int a)
{
	array = new double* [dim];
	for (int i=0;i<dim;i++)
	{
		array[i] = new double [dim];
	}
	if (a==1)
	{
		for (int i=0;i<dim;i++)
		{
			for (int j=0;j<dim;j++)
			{
				array[i][j] = 0;
				if (i==j)
				{
					array[i][j] = 1;
				}
			}
		}
	}
	if (a==0)
	{
		for (int i=0;i<dim;i++)
		{
			for (int j=0;j<dim;j++)
			{
				array[i][j] = 0;
			}
		}
	}
}
Matrix::Matrix()
{
	array = new double* [dim];
	for (int i=0;i<dim;i++)
	{
		array[i] = new double [dim];
	}
	for (int i=0;i<dim;i++)
	{
		for (int j=0;j<dim;j++)
		{
			array[i][j] = 0;
		}
	}
}
Matrix::~Matrix()
{
	for (int i=0;i<dim;i++)
	{
		delete array[i];
	}
	delete [] array;
}
Matrix operator*(double a,const Matrix &m)
{
	Matrix k;
	for (int i=0;i<m.dim;i++)
	{
		for (int j=0;j<m.dim;j++)
		{
			k.array[i][j] = m.array[i][j]*a;
		}
	}
	return k;
}
Matrix operator*(const Matrix &m, double a)
{
	Matrix k;
	for (int i=0;i<m.dim;i++)
	{
		for (int j=0;j<m.dim;j++)
		{
			k.array[i][j] = m.array[i][j]*a;
		}
	}
	return k;
}
ostream &operator<<(ostream &output, const Matrix &m)
{
	for (int i=0;i<m.dim;i++)
	{
		for (int j=0;j<m.dim;j++)
		{
			output << fixed<<setprecision(2) << m.array[i][j]<<" ";
		}
		output << endl;
	}
	return output;
}
Matrix operator+(const Matrix &m,const Matrix &n)
{
	Matrix k;
	for (int i=0;i<m.dim;i++)
	{
		for (int j=0;j<m.dim;j++)
		{
			k.array[i][j] = m.array[i][j] + n.array[i][j];
		}
	}
	return k;
}

double& Matrix::operator() (const int nCol, const int nRow)
{
	assert(nCol >= 0 && nCol < 4);
	assert(nRow >= 0 && nRow < 4);
	return array[nCol][nRow];
}

Matrix operator* (const Matrix &m,const Matrix &n)
{
	Matrix c;
	for (int i=0;i<m.dim;i++)
	{
		for (int j=0;j<m.dim;j++)
		{
			for (int k=0;k<m.dim;k++)
				c.array[i][j] += m.array[i][k]*n.array[k][j];
		}
	}
	return c;
}
Matrix& Matrix::operator+= (const Matrix &n)
{
	for (int i=0;i<dim;i++)
	{
		for (int j=0;j<dim;j++)
		{
			array[i][j] += n.array[i][j];
		}
	}
	return *this;
}
Matrix& Matrix::operator*=(const Matrix &n)
{
	Matrix c;
	int x,y;
	for (int i=0;i<dim;i++)
	{
		x = i;
		for (int j=0;j<dim;j++)
		{
			y = j;
			for (int k=0;k<dim;k++)
				c.array[x][y] += array[x][k]*n.array[k][y];
		}
	}
	for (int i=0;i<dim;i++)
	{
		for (int j=0;j<dim;j++)
		{
			array[i][j] = c.array[i][j];
		}
	}
	return *this;
}
Matrix& Matrix::operator= (const Matrix &p)
{
	if (this != &p)
	{
		for (int i=0;i<dim;i++)
		{
			for (int j=0;j<dim;j++)
			{
				array[i][j] = p.array[i][j];
			}
		}
	}
	return *this;
}
Matrix transpose(Matrix &p)
{
	for (int i=0;i<p.dim;i++)
	{
		for (int j=0;j<p.dim;j++)
		{
			if (j>i)
			{	
				double temp = p.array[i][j];
				p.array[i][j] = p.array[j][i];
				p.array[j][i] = temp;
			}	
		}
	}
	return p;
}