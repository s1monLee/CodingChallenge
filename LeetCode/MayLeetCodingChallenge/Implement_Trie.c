
typedef struct {
    struct Trie* key[26];
    bool isEnd;
} Trie;

/** Initialize your data structure here. */

Trie* trieCreate() {
    Trie* obj = (Trie*)malloc(sizeof(Trie));
    for(int i=0;i<26;i++){
        obj->key[i] = NULL;
    }
    obj->isEnd = false;
    return obj; 
}

/** Inserts a word into the trie. */
void trieInsert(Trie* obj, char * word) {
    Trie* node = obj;
    for(int i=0;i<strlen(word);i++){
        if(node->key[word[i]-'a']==NULL)
            node->key[word[i]-'a'] = trieCreate();
        node = node->key[word[i]-'a'];
    }
    node->isEnd = true;
}

/** Returns if the word is in the trie. */
bool trieSearch(Trie* obj, char * word) {
    Trie* node = obj;
    for(int i=0;i<strlen(word);i++){
        if(node->key[word[i]-'a']==NULL)
            return false;
        node = node->key[word[i]-'a'];
    }
    return node->isEnd == true ? true : false;
}

/** Returns if there is any word in the trie that starts with the given prefix. */
bool trieStartsWith(Trie* obj, char * prefix) {
   Trie* node = obj;
    for(int i=0;i<strlen(prefix);i++){
        if(node->key[prefix[i]-'a']==NULL)
            return false;
        node = node->key[prefix[i]-'a'];
    }
    return true;
}

void trieFree(Trie* obj) {
   
}

/**
 * Your Trie struct will be instantiated and called as such:
 * Trie* obj = trieCreate();
 * trieInsert(obj, word);
 
 * bool param_2 = trieSearch(obj, word);
 
 * bool param_3 = trieStartsWith(obj, prefix);
 
 * trieFree(obj);
*/
