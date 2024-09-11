

// indirect list
// selection sort added

#ifndef IndirectList_
#define IndirectList_

#include <iostream.h>
#include <stdlib.h>
#include "xcept.h"
#include "swap.h"

template <class T> class IndirectListIterator;

template<class T>
class IndirectList {
   friend IndirectListIterator<T>;

   public:
      IndirectList(int MaxListSize = 10); // constructor
      ~IndirectList(); // destructor
      bool IsEmpty() const {return length == 0;}
      int Length() const {return length;}
        // number of elements in list
      bool Find(int k, T& x) const;
        // return k'th element in x
      int Search(const T& x) const;
        // return position of x
      IndirectList<T>& Delete(int k, T& x);
        // delete k'th and return in x
      IndirectList<T>& Insert(int k, const T& x);
        // insert x just after k'th element
      IndirectList<T>& SelectionSort();
        // insert x just after k'th element
      void Output(ostream& out) const;
   private:
      T **table; // 1D array of T pointers
      int length, MaxSize;
};

template<class T>
IndirectList<T>::IndirectList(int MaxListSize)
{// Constructor.
   MaxSize = MaxListSize;
   table = new T *[MaxSize];
   length = 0;
}

template<class T>
IndirectList<T>::~IndirectList()
{// Delete the list.
   for (int i = 0; i < length; i++)
      delete table[i];
   delete [] table;
}

template<class T>
bool IndirectList<T>::Find(int k, T& x) const
{// Set x to the k'th element in the chain.
 // Return false if no k'th; return true otherwise.
   if (k < 1 || k > length) return false; // no k'th
   x = *table[k - 1];
   return true;
}

template<class T>
int IndirectList<T>::Search(const T& x) const
{// Locate x.  Return position of x if found.
 // Return 0 if x not in the chain.
   for (int i = 0; i < length; i++)
      if (*table[i] == x) return ++i;
   return 0;
}

template<class T>
IndirectList<T>& IndirectList<T>::Delete(int k, T& x)
{// Set x to the k'th element and delete it.
 // Throw OutOfBounds exception if no k'th element.
   if (Find(k, x)) {// move pointers k+1, ..., down
      for (int i = k; i < length; i++)
         table[i-1] = table[i];
      length--;
      return *this;
      }
   else throw OutOfBounds();
}

template<class T>
IndirectList<T>& IndirectList<T>::Insert(int k, const T& x)
{// Select x after the k'th element.
 // Throw OutOfBounds exception if no k'th element.
 // Pass NoMem exception if inadequate space.
   if (k < 0 || k > length) throw OutOfBounds();
   if (length == MaxSize) throw NoMem();
   // move one up
   for (int i = length-1; i >= k; i--)
      table[i+1] = table[i];
   table[k] = new T;
   *table[k] = x;
   length++;
   return *this;
}

template<class T>
IndirectList<T>& IndirectList<T>::SelectionSort()
{// Sort using the selection-sort method.
 // Early-terminating version.
   bool sorted = false;
   for (int size = length; !sorted && (size > 1); size--) {
      int pos = 0;
      sorted = true;
      // find largest
      for (int i = 1; i < size; i++)
         if (*table[pos] <= *table[i]) pos = i;
         else sorted = false; // out of order
      Swap(table[pos], table[size - 1]);
      }
   return *this;
}

template<class T>
void IndirectList<T>::Output(ostream& out) const
{
   for (int i=0; i < length; i++)
     out << *table[i] << "  ";
}

// overload <<
template <class T>
ostream& operator<<(ostream& out, const IndirectList<T>& x)
   {x.Output(out); return out;}

#endif
